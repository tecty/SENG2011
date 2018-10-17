<template>
  <v-card :to="{ name: 'EventDetail', params: { eventId: event.id }}">
    <v-card-title primary-title>
      <h4>{{event.title}}</h4>
    </v-card-title>
    <v-divider />
    <v-list >
      <v-list-tile>
        <v-list-tile-content>Issuer:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ event.owner.username }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>Event Time:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ event.eventTime }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>Bid End:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ event.bidClosingTime }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>Location:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ event.location.address }}
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-card>
</template>

<script>
export default {
  // the data of this event
  props: ["event"],
  data() {
    return {
      offer: ""
    };
  }
};
</script>
