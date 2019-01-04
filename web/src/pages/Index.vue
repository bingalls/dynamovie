<template>
  <q-page class="flex flex-center">
    <!-- <img alt="Quasar logo" src="~assets/quasar-logo-full.svg"> -->
    <q-table
      title="Movies"
      :data="serverData"
      :columns="columns"
      row-key="name"
    />
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
        style: 'width: 10rem',
      },
      {
        name: 'studio',
        required: true,
        label: 'Studio',
        align: 'left',
        field: 'studio',
        sortable: true,
        classes: 'movies',
        style: 'width: 10rem',
      },
      {
        name: 'director',
        required: true,
        label: 'Director',
        align: 'left',
        field: 'director',
        sortable: true,
        classes: 'movies',
        style: 'width: 10rem',
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
      // {
      //   title: 'Furious 7',
      //   genre: 'Action',
      //   studio: 'Universal',
      //   director: 'James Wan',
      //   actor: 'Jordana Brewster',
      // },
      // {
      //   title: 'Star Wars',
      //   genre: 'Science Fiction',
      //   studio: 'Disney',
      //   director: 'JJ Abrams',
      //   actor: 'Mark Hammil',
      // },
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
          console.dir(data.list); // eslint-disable-line no-console
          // updating pagination to reflect in the UI
          this.serverPagination = pagination;

          // we also set (or update) rowsNumber
          // this.serverPagination.rowsNumber = data.list.rowsNumber;
          this.serverPagination.rowsNumber = 5; // FIXME

          // then we update the rows with the fetched ones
          // this.serverData = data.list.rows;
          this.serverData = data.list;

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
