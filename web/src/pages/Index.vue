<template>
  <q-page class="flex flex-center">
    <!-- <img alt="Quasar logo" src="~assets/quasar-logo-full.svg"> -->
    <q-collapsible icon="search" label="Search Movie">
      <form>
        <q-input v-model="search" stack-label="Title" />
        <br />
        <!-- <q-select v-model="select" float-label="Movie Genre" :options="genres" /> -->
        <Select>
          <Option value="All" key="All">All</Option>
          <Option value="Action" key="Action">Action</Option>
          <Option value="Science Fiction" key="Science Fiction">Science Fiction</Option>
        </Select>
        <q-input v-model="search" stack-label="Studio" />
        <q-input v-model="search" stack-label="Director" />
        <q-input v-model="search" stack-label="Actor" />
        <q-btn icon="search" label="Search" @click="search" />
      </form>
    </q-collapsible>

    <q-table
      title="Movies"
      :data="serverData"
      :columns="columns"
      row-key="name"
    />

    <q-collapsible icon="plus" label="Add Movie">
      <form>
        <q-input v-model="text" stack-label="Title" />
        <br />
        <!-- <q-select v-model="select" float-label="Movie Genre" :options="genres" /> -->
        <Select>
          <Option value="Action" key="Action">Action</Option>
          <Option value="Science Fiction" key="Science Fiction">Science Fiction</Option>
        </Select>
        <q-input v-model="text" stack-label="Studio" />
        <q-input v-model="text" stack-label="Director" />
        <q-input v-model="text" stack-label="Actor" />
        <q-btn icon="create" label="Add" @click="addMovie" />
      </form>
    </q-collapsible>
  </q-page>
</template>

<style>
</style>

<script>
import axios from 'axios';

export default {
  data: () => ({
    filter: '',
    loading: false,
    serverPagination: {
      page: 1,
      rowsNumber: 10, // specifying this determines pagination is server-side
    },
    genres: [
      {
        label: 'Action',
        value: 'Action',
      },
      {
        label: 'Science Fiction',
        value: 'Science Fiction',
      },
    ],
    columns: [
      {
        name: 'title',
        required: true,
        label: 'Movie Title',
        align: 'left',
        field: 'title',
        sortable: true,
        classes: 'movies',
        style: 'width: 10rem',
      },
      {
        name: 'genre',
        required: true,
        label: 'Genre',
        align: 'left',
        field: 'genre',
        sortable: true,
        classes: 'movies',
        style: 'width: 8rem',
      },
      {
        name: 'studio',
        required: true,
        label: 'Studio',
        align: 'left',
        field: 'studio',
        sortable: true,
        classes: 'movies',
        style: 'width: 8rem',
      },
      {
        name: 'director',
        required: true,
        label: 'Director',
        align: 'left',
        field: 'director',
        sortable: true,
        classes: 'movies',
        style: 'width: 8rem',
      },
      {
        name: 'actor',
        required: true,
        label: 'Actor',
        align: 'left',
        field: 'actor',
        sortable: true,
        classes: 'movies',
        style: 'width: 10rem',
      },
    ],
    serverData: [
      {
        title: 'Server Down',
        genre: 'Error',
        studio: 'Call Support',
        director: 'info@example.com',
        actor: 'Try Later',
      },
    ],
  }),
  name: 'PageIndex',

  methods: {
    request({ pagination }) {
      // ', filter' we set QTable to "loading" state
      this.loading = true;

      // we do the server data fetch, based on pagination and filter received
      // (using Axios here, but can be anything; parameters vary based on backend implementation)
      // eslint-disable-next-line no-undef
      axios
        .get('http://127.0.0.1:8000/movies/')
        .then(({ data }) => {
          // console.dir(data); // eslint-disable-line no-console
          // updating pagination to reflect in the UI
          this.serverPagination = pagination;

          // we also set (or update) rowsNumber
          this.serverPagination.rowsNumber = data.rowsNumber;

          // then we update the rows with the fetched ones
          // this.serverData = data.data.rows;
          this.serverData = data.data;

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
      console.log('todo');
    },
    search(evt) {
      console.log(search.value);
    },
  },
  mounted() {
    // once mounted, we need to trigger the initial server data fetch
    this.request({
      pagination: this.serverPagination,
      filter: this.filter,
    });
  },
};
</script>
