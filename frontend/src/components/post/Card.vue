<template>
  <v-card :to="{ name: 'BidCreate', params: { postId: post.id }}">
    <v-card-title primary-title>
      <h4>{{post.title}} of {{post.event.title}}</h4>
    </v-card-title>
    <v-divider />
    <v-list >
      <v-list-tile>
        <v-list-tile-content>Issuer:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ post.event.owner.username }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>Event Time:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ post.event.eventTime }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>Bid End:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ post.event.bidClosingTime }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>People Occuation:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ post.peopleCount }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>Budget:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          ${{ post.budget }}
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>Bid Count:</v-list-tile-content>
        <v-list-tile-content class="align-end">
          {{ post.bid_set.length }}
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-card>
</template>

<script>
export default {
  // the data of this post
  props: ["post"],
  data() {
    return {
      offer: ""
    };
  }
};
</script>
