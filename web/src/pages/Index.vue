<template>
  <q-page class="flex flex-center">
    <!-- <q-select v-model="selectCriteria" float-label="Search For"
      :options="searchCriteria" /> -->
    <select>
      <Option value="Title" key="Title">Title</Option>
      <Option value="Genre" key="Genre">Genre</Option>
      <Option value="Studio" key="Studio">Studio</Option>
      <Option value="Director" key="Director">Director</Option>
      <Option value="Actor" key="Actor">Actor</Option>
    </select>

    <q-search  /> <!-- v-model="search" -->

    <q-table
      title="Movies"
      :data="serverData"
      :columns="columns"
      row-key="title"
      :selection="selection"
      :selected.sync="selected"
    >
      <template slot="top-selection" slot-scope="props">
        <q-btn color="secondary" flat round delete icon="edit" @click="editRow" />
        <div class="col" />
        <q-btn color="negative" flat round delete icon="delete" @click="deleteRow" />
      </template>
    </q-table>

    <q-collapsible icon="plus" label="Add Movie">
      <form>
        <q-input stack-label="Title" /> <!-- v-model="text" -->
        <br />
        <!-- <q-select v-model="select" float-label="Movie Genre" :options="genres" /> -->
        <Select>
          <Option value="Action" key="Action">Action</Option>
          <Option value="Science Fiction" key="Science Fiction">Science Fiction</Option>
        </Select>
        <q-input stack-label="Studio" />
        <q-input stack-label="Director" />
        <q-input stack-label="Actor" />
        <q-btn icon="add" label="Add" @click="addMovie" />
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
    selection: 'single',
    selected: [{ title: '' }],
    serverPagination: {
      page: 1,
      rowsNumber: 10, // specifying this determines pagination is server-side
    },
    genres: [
      { label: 'Action', value: 'Action' },
      { label: 'Science Fiction', value: 'Science Fiction' },
    ],
    // searchCriteria: [
    //   { label: 'Title', value: 'Title' },
    //   { label: 'Genre', value: 'Genre' },
    //   { label: 'Studio', value: 'Studio' },
    //   { label: 'Director', value: 'Director' },
    //   { label: 'Actor', value: 'Actor' },
    // ],
    columns: [
      {
        name: 'title',
        required: true,
        label: 'Movie Title',
        field: 'title',
        sortable: true,
        style: 'width: 9rem',
      },
      {
        name: 'genre',
        required: true,
        label: 'Genre',
        field: 'genre',
        sortable: true,
        style: 'width: 7rem',
      },
      {
        name: 'studio',
        required: true,
        label: 'Studio',
        field: 'studio',
        sortable: true,
        style: 'width: 7rem',
      },
      {
        name: 'director',
        required: true,
        label: 'Director',
        field: 'director',
        sortable: true,
        style: 'width: 7rem',
      },
      {
        name: 'actors',
        required: true,
        label: 'Actors',
        field: 'actors',
        sortable: true,
        style: 'width: 15rem',
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
          this.serverData = data.rows;

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
    search() {
      console.log('todo');
      // console.log(search.value);
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
