<template>
  <!-- The AG Grid component -->
  <ag-grid-vue
    :rowData="rowData"
    :columnDefs="colDefs"
    :style="style"
    :localeText="localeText"
    class="ag-theme-quartz"
    @cell-value-changed="onCellValueChanged"
  >
  </ag-grid-vue>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { Streamlit } from 'streamlit-component-lib'
import { useStreamlit } from './streamlit'
import 'ag-grid-community/styles/ag-grid.css' // Mandatory CSS required by the Data Grid
import 'ag-grid-community/styles/ag-theme-quartz.css' // Optional Theme applied to the Data Grid
import { AgGridVue } from 'ag-grid-vue3' // Vue Data Grid Component
import { AG_GRID_LOCALE_BR } from '@ag-grid-community/locale'

export default {
  name: 'CustomAgGrid',
  props: ['args'], // Arguments that are passed to the plugin in Python are accessible in prop "args"
  components: {
    AgGridVue // Add Vue Data Grid component
  },
  setup(props) {
    useStreamlit()
    // Row Data: The data to be displayed.
    const rowData = computed(() => props.args.rowData)

    // Column Definitions: Defines the columns to be displayed.
    const colDefs = computed(() => props.args.colDefs)

    const style = computed(() => props.args.style)

    const localeText = ref({}) // Placeholder for the dynamically loaded locale

    const loadLocale = async () => {
      try {
        const module = await import('@ag-grid-community/locale')
        localeText.value = module[props.args.localeText]
      } catch (error) {
        console.error(`Failed to load locale ${props.locale}:`, error)
      }
    }

    // Load the locale when the component is mounted
    onMounted(() => {
      loadLocale()
    })

    const onCellValueChanged = (event) => {
      // Example: Send updated data back to Streamlit or handle it otherwise
      Streamlit.setComponentValue({
        index: event.rowIndex,
        field: event.colDef.field,
        oldValue: event.oldValue,
        newValue: event.newValue,
        data: event.data
      })
    }

    return {
      rowData,
      colDefs,
      style,
      localeText,
      onCellValueChanged
    }
  }
}
</script>
