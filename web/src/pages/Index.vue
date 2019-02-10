<template>
  <q-page class="flex flex-center">
    <!-- Search box. Moving this to the title bar, puts the model scope in a new component -->
    <form class="flexbox">
      <!-- <q-select :options="selectCriteria" v-model="genre"  /> -->
      <q-select :options="selectCriteria" v-model="currentCrit"  />
      <q-input class="col" clearable placeholder="keyword" v-model="keyword"
       @keydown.enter="search" />
      <q-btn color="primary" icon="search" :loading="loading" round type="submit" @click="search" />
    </form>

    <!-- todo :pagination.sync="serverPagination" -->
    <q-table
      :columns="columns"
      :data="serverData"
      row-key="title"
      title="Movies"
    >
      <q-tr slot="body" slot-scope="props" :props="props">
        <q-td key="title" :props="props">{{ props.row.title }}
          <q-popup-edit :data-id="props.row.title" :props="props" v-model="props.row.title"
           v-on:save="editMovie($event, props.row, 'title')">
            <q-field><q-input v-model="props.row.title" /></q-field>
          </q-popup-edit>
        </q-td>
        <q-td key="genre" :props="props">
          <q-select v-model="props.row.genre" :options="genres" />
          <q-popup-edit :data-id="props.row.title" :props="props" v-model="props.row.genre"
            title="Update genre" buttons>
            <q-select :data-id="props.row.title" float-label="Movie Genre" :options="genres"
             v-model="props.row.genre" v-on:input="editMovie($event, props.row, 'genre')" />
          </q-popup-edit>
        </q-td>
        <q-td key="studio" :props="props">
          <q-select v-model="props.row.studio" :options="studios" />
          <q-popup-edit :data-id="props.row.title" :props="props" title="Update studio" buttons>
            <q-select :data-id="props.row.title" float-label="Studio" :options="studios"
              v-model="props.row.studio" v-on:input="editMovie($event, props.row, 'studio')" />
          </q-popup-edit>
        </q-td>
        <q-td key="director" :props="props">{{ props.row.director }}
          <q-popup-edit :data-id="props.row.title" :props="props" v-model="props.row.director"
           v-on:save="editMovie($event, props.row, 'director')">
            <q-field><q-input v-model="props.row.director" /></q-field>
          </q-popup-edit>
        </q-td>
        <q-td key="actors" :data-id="props.row.title" :props="props">{{ props.row.actors }}
          <q-popup-edit :data-id="props.row.title" :props="props" v-model="props.row.actors"
           v-on:save="editMovie($event, props.row, 'actors')">
            <q-field><q-input v-model="props.row.actors" /></q-field>
          </q-popup-edit>
        </q-td>
        <q-td key="delkey" :props="props">
          <!-- <q-btn flat round delete icon="delete" v-model="props.row.title"
          @click="deleteMovie" label="props.row.title" /> -->

          <q-collapsible icon="delete">
            <form>
              <!-- <input type="hidden" name="title" value="{{rops.row.title}}"
                v-model="props.row.title" /> -->
              <q-input name="todelete" readonly v-model="title" value="props.row.title" />
              <q-btn :data-id="props.row.title" icon="delete" label="Confirm"
               @click="deleteMovie" :value="props.row.title" />
            </form>
          </q-collapsible>
        </q-td>
      </q-tr>
    </q-table>

    <q-collapsible icon="plus" label="Add Movie">
      <form>
        <q-input stack-label="Title" v-model="title" />
        <br />
        <q-select v-model="currentGenre" float-label="Movie Genre" :options="genres" />
        <q-select v-model="currentStudio" float-label="Studio" :options="studios" />
        <q-input stack-label="Director" v-model="director" />
        <q-input stack-label="Actors" v-model="actors" />
        <q-btn icon="add" label="Add" @click="addMovie" />
      </form>
    </q-collapsible>
  </q-page>
</template>

<style>
.flexbox {
  display: flex;
}
.col {
  margin: 0 0.25rem;
}
/* Fixing Quasar v0.17.19 bug? Font in select elements was larger than table text */
.q-input-target, .q-input-shadow {
  font-size: 0.9rem
}
</style>

<script>
import axios from 'axios';

export default {
  data: () => ({
    actors: '',
    currentCrit: 'genre',
    currentGenre: 'Action',
    currentStudio: 'independent',
    director: '',
    filter: '',
    keyword: '',
    loading: false,
    selection: 'single',
    selected: [{ title: '' }],
    title: '',
    url: 'http://127.0.0.1:8000',
    // serverPagination: {
    //   page: 1,
    //   rowsNumber: 10, // specifying this determines pagination is server-side
    // },
    genres: [
      { label: 'Action', value: 'Action' },
      { label: 'Horror', value: 'Horror' },
      { label: 'Science Fiction', value: 'Science Fiction' },
    ],
    selectCriteria: [
      { label: 'Title', value: 'title' },
      { label: 'Genre', value: 'genre' },
      { label: 'Studio', value: 'studio' },
      { label: 'Director', value: 'director' },
      { label: 'Actor', value: 'actors' },
    ],
    studios: [
      { label: 'Disney', value: 'Disney' },
      { label: 'Elevation', value: 'Elevation' },
      { label: 'independent', value: 'independent' },
      { label: 'Lucas Films', value: 'Lucas Films' },
      { label: 'Marvel', value: 'Marvel' },
      { label: 'Universal', value: 'Universal' },
    ],
    columns: [
      {
        field: 'title', label: 'Movie Title', name: 'title', required: true, sortable: true, style: 'width: 9rem',
      },
      {
        field: 'genre', label: 'Genre', name: 'genre', required: true, sortable: true, style: 'width: 7rem',
      },
      {
        field: 'studio', label: 'Studio', name: 'studio', required: true, sortable: true, style: 'width: 7rem',
      },
      {
        field: 'director', label: 'Director', name: 'director', required: true, sortable: true, style: 'width: 7rem',
      },
      {
        field: 'actors', label: 'Actors', name: 'actors', required: true, sortable: true, style: 'width: 15rem',
      },
      {
        field: 'delkey', label: '', name: 'delkey', required: true, sortable: false, style: 'width: 1rem',
      },
    ],
    serverData: [
      {
        title: 'Server Down', genre: 'Error', studio: 'Call Support', director: 'info@example.com', actors: 'Try Later',
      },
    ],
  }),
  name: 'PageIndex',

  methods: {
    request(filter, query = '') { // todo { pagination } param
      this.loading = true; // set QTable to "loading" state

      // do the server data fetch, based on pagination and filter received
      // eslint-disable-next-line no-undef
      axios
        .get(`${this.url}/movies/${query}`)
        .then(({ data }) => {
          // this.serverPagination = pagination;
          // this.serverPagination.rowsNumber = data.rowsNumber;

          this.serverData = data.rows;
          this.loading = false; // exit QTable loading state
        })
        .catch((error) => {
          this.loading = false; // exit QTable loading state
          console.warn(error); // eslint-disable-line no-console
        });
    },
    addMovie() {
      this.loading = true; // set QTable to "loading" state
      axios
        .put(`${this.url}/movies/`, {
          actors: [this.actors],
          director: this.director,
          genre: this.currentGenre,
          studio: this.currentStudio,
          title: this.title,
        })
        .then(({ data }) => {
          this.serverData = data.rows;
          this.loading = false; // exit QTable loading state
        })
        .catch((error) => {
          this.loading = false; // exit QTable loading state
          console.warn(error); // eslint-disable-line no-console
        });
    },
    deleteMovie(event) {
      this.loading = true; // set QTable to "loading" state
      axios
        .delete(`${this.url}/movie/${event.currentTarget.getAttribute('data-id')}`)
        .then(() => {
          this.search({});
          this.loading = false; // exit QTable loading state
        })
        .catch((error) => {
          this.loading = false; // exit QTable loading state
          console.warn(error); // eslint-disable-line no-console
        });
    },
    editMovie(target, id, column) {
      const formData = {
        oldtitle: id.title,
        newtitle: id.title,
        genre: id.genre,
        studio: id.studio,
        director: id.director,
        actors: [id.actors],
      };

      if (column === 'title') {
        formData.newtitle = target;
      }
      if (column === 'actors') {
        formData.actors = [target];
      }

      this.loading = true; // set QTable to "loading" state
      axios
        .post(`${this.url}/movies/`, formData)
        .then(({ data }) => {
          this.serverData = data.rows;
          this.loading = false; // exit QTable loading state
        })
        .catch((error) => {
          this.loading = false; // exit QTable loading state
          console.warn(error); // eslint-disable-line no-console
        });
    },
    search() {
      this.request(null, `?cat=${this.currentCrit}&search=${encodeURIComponent(this.keyword)}`);
    },
  },
  mounted() {
    // once mounted, we need to trigger the initial server data fetch
    this.search({});
  },
};
</script>
