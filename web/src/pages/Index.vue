<template>
  <q-page class="flex flex-center">
    <form class="flexbox">
      <q-select :options="selectCriteria" v-model="currentCrit"  />
      <q-input class="col" clearable placeholder="keyword" v-model="keyword" />
      <q-btn @click="search" color="primary" icon="search" :loading="loading" round type="submit" />
    </form>

      <!-- :pagination.sync="serverPagination" -->
    <q-table
      :columns="columns"
      :data="serverData"
      :selected.sync="selected"
      :selection="selection"
      row-key="title"
      title="Movies"
    >
      <template slot="top-selection" slot-scope="props">
        <q-btn color="secondary" flat round delete icon="edit" @click="editMovie" />
        <div class="col" />
        <q-btn color="negative" flat round delete icon="delete" @click="deleteMovie" />
      </template>
    </q-table>

    <q-collapsible icon="plus" label="Add Movie">
      <form>
        <q-input stack-label="Title" value="" /> <!-- v-model="text" -->
        <br />
        <q-select v-model="currentGenre" float-label="Movie Genre" :options="genres" />
        <q-input stack-label="Studio" value="" />
        <q-input stack-label="Director" value="" />
        <q-input stack-label="Actor" value="" />
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
</style>

<script>
import axios from 'axios';

export default {
  data: () => ({
    currentCrit: 'genre',
    currentGenre: 'Action',
    filter: '',
    keyword: '',
    loading: false,
    selection: 'single',
    selected: [{ title: '' }],
    // serverPagination: {
    //   page: 1,
    //   rowsNumber: 10, // specifying this determines pagination is server-side
    // },
    genres: [
      { label: 'Action', value: 'Action' },
      { label: 'Science Fiction', value: 'Science Fiction' },
    ],
    selectCriteria: [
      { label: 'Title', value: 'title' },
      { label: 'Genre', value: 'genre' },
      { label: 'Studio', value: 'studio' },
      { label: 'Director', value: 'director' },
      { label: 'Actor', value: 'actor' },
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
    ],
    serverData: [
      {
        title: 'Server Down', genre: 'Error', studio: 'Call Support', director: 'info@example.com', actor: 'Try Later',
      },
    ],
  }),
  name: 'PageIndex',

  methods: {
    // request({ pagination }) {
    request(filter, query = '') {
      // set QTable to "loading" state
      this.loading = true;

      // do the server data fetch, based on pagination and filter received
      // (using Axios here, but can be anything; parameters vary based on backend implementation)
      // eslint-disable-next-line no-undef
      axios
        .get(`http://127.0.0.1:8000/movies/${query}`)
        .then(({ data }) => {
          // console.dir(data); // eslint-disable-line no-console
          // updating pagination to reflect in the UI
          // this.serverPagination = pagination;

          // we also set (or update) rowsNumber
          // this.serverPagination.rowsNumber = data.rowsNumber;

          // then we update the rows with the fetched ones
          // if (keyword === '') {
          this.serverData = data.rows;
          // } else {
          //   this.serverData = data.rows.filter((row) => { // eslint-disable-line arrow-body-style
          //     return Object.values(row).some((col) => { // eslint-disable-line arrow-body-style
          //       return col.includes(keyword);
          //     });
          //   });
          // }

          // finally we tell QTable to exit the "loading" state
          this.loading = false;
        })
        .catch((error) => {
          // there's an error... do SOMETHING

          // we tell QTable to exit the "loading" state
          this.loading = false;
          console.warn(error); // eslint-disable-line no-console
        });
    },
    addMovie() {
      // console.log('todo');
    },
    deleteMovie(title) {
      axios
        .delete(`http://127.0.0.1:8000/movies/?title=${title}`)
        .then(({ data }) => {
          this.serverData = data.rows;
          // this.loading = false;
        })
        .catch((error) => {
          // we tell QTable to exit the "loading" state
          // this.loading = false;
          console.warn(error); // eslint-disable-line no-console
        });
    },
    editMovie(title) {
      axios
        .post(`http://127.0.0.1:8000/movies/?title=${title}`)
        .then(({ data }) => {
          this.serverData = data.rows;
          // this.loading = false;
        })
        .catch((error) => {
          // we tell QTable to exit the "loading" state
          // this.loading = false;
          console.warn(error); // eslint-disable-line no-console
        });
    },
    search() {
      this.request(null, `?col=${this.currentCrit}&search=${encodeURIComponent(this.keyword)}`);
    },
  },
  mounted() {
    // once mounted, we need to trigger the initial server data fetch
    this.request({
      // pagination: this.serverPagination,
      filter: this.filter,
    });
  },
};
</script>
