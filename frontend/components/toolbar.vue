<template>
  <v-app-bar color="rgb(255,0,0)" class="yellow--text" dark fixed app clipped-right>
    <v-app-bar-nav-icon @click.stop="state.drawer = !state.drawer" />
    <v-layout justify-center align-center>
      <v-btn icon color="light-green" href="https://web.whatsapp.com/send?phone=551299702-9059" target="_blank">
        <v-icon>mdi-whatsapp</v-icon>
      </v-btn>
      <v-toolbar-title>Mercado Santa Inês</v-toolbar-title>
      <v-btn icon color="light-blue" href="https://www.facebook.com/Mercado-Santa-Ines-109802760942900" target="_blank">
        <v-icon>mdi-facebook</v-icon>
      </v-btn>
    </v-layout>
  </v-app-bar>
</template>

<script>
import Snacks from '~/helpers/Snacks.js'
import api from '~api'
export default {
  props: ['state'],
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  methods: {
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    },
    async logout () {
      await api.logout()
      this.$store.commit('auth/setCurrentUser', null)
      Snacks.show(this.$store, {text: 'Até logo!'})
    }
  }
}
</script>
