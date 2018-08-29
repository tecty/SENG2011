<template>
  <v-content>
      <v-card flat >
      <v-snackbar
        v-model="snackbar"
        absolute
        top
        right
        color="success"
      >
        <span>Post successful!</span>
        <v-icon dark>check_circle</v-icon>
      </v-snackbar>
  <v-form ref="form"  @submit.prevent="submit">
    <v-container grid-list-xl fluid>
    <v-layout wrap >
    <v-text-field
      v-model="form.title"
      :rules="rules.name"
      label="Title"
      required
    ></v-text-field>
      <v-flex xs12>
        <v-textarea
          v-model="form.msg"
          color="teal"
        >
          <div slot="label">
            Description 
          </div>
        </v-textarea>
      </v-flex>
    
<v-flex xs12 sm6 md4>
      <v-menu
        ref="menu"
        :close-on-content-click="false"
        v-model="form.menu"
        :nudge-right="40"
        :return-value.sync="date"
        lazy
        transition="scale-transition"
        offset-y
        full-width
        min-width="290px"
      >
        <v-text-field
          slot="activator"
          v-model="form.date"
          label="Event Date"
          prepend-icon="event"
          readonly
          required
        ></v-text-field>
        <v-date-picker v-model="form.date" no-title scrollable>
          <v-spacer></v-spacer>
          <v-btn flat color="primary" @click="$refs.menu.save(form.date)">OK</v-btn>
        </v-date-picker>
      </v-menu>
</v-flex>
<v-flex xs11 sm5>
      <v-menu
        ref="menu"
        :close-on-content-click="false"
        v-model="form.menu2"
        :nudge-right="40"
        :return-value.sync="form.time"
        lazy
        transition="scale-transition"
        offset-y
        full-width
        max-width="290px"
        min-width="290px"
      >
        <v-text-field
          slot="activator"
          v-model="form.time"
          label="Event Time"
          prepend-icon="access_time"
          readonly
          required
        ></v-text-field>
        <v-time-picker
          v-if="form.menu2"
          v-model="form.time"
          @change="$refs.menu.save(form.time)"
        ></v-time-picker>
      </v-menu>
</v-flex>
      </v-layout>
    </v-container>

          <v-card-actions>
        <v-btn flat @click="resetForm">Clear</v-btn>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!formIsValid"
          flat
          color="primary"
          type="submit"
        >Post</v-btn>
</v-card-actions>
  </v-form>
           </v-card>
  </v-content>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      const defaultForm = Object.freeze({
        title: '',
        name: '',
        msg: '',
        favoriteAnimal: '',
        age: null,
        terms: false,
        date: null,
        menu: false,
        time: null,
        menu2: false,
      })

      return {
        form: Object.assign({}, defaultForm),
        rules: {
          age: [
            val => val < 10 || `I don't believe you!`
          ],
          animal: [val => (val || '').length > 0 || 'This field is required'],
          name: [val => (val || '').length > 0 || 'This field is required']
        },
        animals: ['Dog', 'Cat', 'Rabbit', 'Turtle', 'Snake'],
        conditions: false,
        content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc.`,
        snackbar: false,
        terms: false,
      }
    },
    computed: {
        formIsValid () {
          return (
            this.form.title
          )
        }
      },

      methods: {
        resetForm () {
          this.form = Object.assign({}, this.defaultForm)
          this.$refs.form.reset()
        },
        submit () {
          this.snackbar = true
          this.resetForm()
        }
      }
  }
</script>