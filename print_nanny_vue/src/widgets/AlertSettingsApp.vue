<script>
import ProgressAlertSettings from '@/components/ProgressAlertSettings'
import DefectAlertSettings from '@/components/DefectAlertSettings'
import CommandAlertSettings from '@/components/CommandAlertSettings'
import { mapState, mapActions } from 'vuex'

import { FETCH_ALERT_METHODS, SETTINGS_MODULE, ALERT_METHODS } from '@/store/settings'
export default {
  name: 'AlertSettingsApp',
  components: { ProgressAlertSettings, DefectAlertSettings, CommandAlertSettings },
  methods: {
    ...mapActions(SETTINGS_MODULE, {
      fetchAlertMethods: FETCH_ALERT_METHODS
    })
  },
  computed: {
    ...mapState(SETTINGS_MODULE, {
      alert_methods: ALERT_METHODS
    })
  },
  created () {
    this.fetchAlertMethods()
  }
}
</script>

<template>
    <div>
        <ProgressAlertSettings v-for="item in alert_methods" :key="item.value">

        </ProgressAlertSettings>
        <DefectAlertSettings v-for="item in alert_methods" :key="item.value">

        </DefectAlertSettings>
        <CommandAlertSettings v-for="item in alert_methods" :key="item.value">

        </CommandAlertSettings>
    </div>
</template>
