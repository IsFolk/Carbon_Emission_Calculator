<template>
  <h1>試著跑跑看IRIS</h1>
  <n-message-provider>
    <UserProfile/>
  </n-message-provider>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import UserProfile from "./components/UserProfile.vue"
import FormInput from "./components/FormInput.vue"



export default defineComponent({
  name: 'App',
  components: {
    UserProfile,
    // FormInput
  }
});
</script>
