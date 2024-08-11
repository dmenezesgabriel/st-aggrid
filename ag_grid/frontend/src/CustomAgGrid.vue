<template>
  <!-- The AG Grid component -->
  <ag-grid-vue
    :rowData="rowData"
    :columnDefs="colDefs"
    :style="style"
    class="ag-theme-quartz"
    @cell-value-changed="onCellValueChanged"
  >
  </ag-grid-vue>
</template>

<script>
import { ref } from 'vue'
import { Streamlit } from 'streamlit-component-lib'
import { useStreamlit } from './streamlit'
import 'ag-grid-community/styles/ag-grid.css' // Mandatory CSS required by the Data Grid
import 'ag-grid-community/styles/ag-theme-quartz.css' // Optional Theme applied to the Data Grid
import { AgGridVue } from 'ag-grid-vue3' // Vue Data Grid Component

export default {
  name: 'CustomAgGrid',
  props: ['args'], // Arguments that are passed to the plugin in Python are accessible in prop "args"
  components: {
    AgGridVue // Add Vue Data Grid component
  },
  setup(props) {
    useStreamlit()
    // Row Data: The data to be displayed.
    const rowData = ref(props.args.rowData)

    // Column Definitions: Defines the columns to be displayed.
    const colDefs = ref(props.args.colDefs)

    const style = ref(props.args.style)

    const onCellValueChanged = (event) => {
      console.log('Cell Value Changed', event)
      // You can access the row and column that was edited, as well as the new and old values
      console.log('Row Index:', event.rowIndex)
      console.log('Column:', event.colDef.field)
      console.log('Old Value:', event.oldValue)
      console.log('New Value:', event.newValue)

      // Example: Send updated data back to Streamlit or handle it otherwise
      Streamlit.setComponentValue(event.data)
    }

    return {
      rowData,
      colDefs,
      style,
      onCellValueChanged
    }
  }
}
</script>
