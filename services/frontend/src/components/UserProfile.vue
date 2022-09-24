<template>
  <n-form :model="model">
    <n-dynamic-input v-model:value="model.dynamicInputValue" item-style="margin-bottom: 0;" :on-create="onCreate"
      #="{ index, value }">
      <div style="display: flex">
        <!--
          Usually, the path change will cause the form-item verification content
          or rules to be changed, so naive-ui will clear the existing
          verification effect. But this example is a special case, as we know
          the changes in path will not change form-item verification result and
          rules, so set ignore-path-change on form-item
        -->
        <n-form-item ignore-path-change :show-label="false" :path="`dynamicInputValue[${index}].name`"
          :rule="dynamicInputRule">
          <n-input v-model:value="model.dynamicInputValue[index].name" placeholder="Name" @keydown.enter.prevent />
          <!--
           Since pressing enter on the input element will cause the button in the form to be clicked, the default behavior is prevented
          -->
        </n-form-item>
        <div style="height: 34px; line-height: 34px; margin: 0 8px">
          =
        </div>
        <n-form-item ignore-path-change :show-label="false" :path="`dynamicInputValue[${index}].value`"
          :rule="dynamicInputRule">
          <n-input v-model:value="model.dynamicInputValue[index].value" placeholder="Value" @keydown.enter.prevent />
        </n-form-item>
      </div>
    </n-dynamic-input>
  </n-form>
  <n-button type="success" @click="apicall">
    Run
  </n-button>
  <p>結果:{{msg}}</p>
  <pre>{{ JSON.stringify(model.dynamicInputValue, null, 2) }}</pre>
</template>

<script lang="ts">
import { defineComponent, ref, inject, toRaw } from 'vue'
import { FormRules, useMessage } from 'naive-ui'


interface ModelType {
  sepal_length: number | null
  sepal_width: number | null
  petal_length: number | null
  petal_width: number | null
}

export default defineComponent({
  setup() {

    const axios: any = inject('axios')
    axios.defaults.withCredentials = true

    const message = useMessage()
    const msg = ref()
    const model = ref({
      dynamicInputValue: [{ value: '', name: '' }]
    })


    const apicall = () => {
      const data = toRaw(model.value.dynamicInputValue)
      console.log(data)
      message.info('Button Clicked')

      axios.post('/predict-result', {
        content: JSON.stringify(data)
      }, {
        headers: {
          'Content-type': 'application/json',
        }
      }).then((res: any) => {
        msg.value = res.data
      }).catch((error: any) => {
        console.log(error)
      })
    }

    return {
      dynamicInputRule: {
        trigger: 'input',
        validator(rule: unknown, value: string) {
          if (!value) return new Error('Need Input')
          return true
        }
      },
      model,
      onCreate() {
        return {
          name: '',
          value: ''
        }
      },
      msg,
      apicall
    }
  }
})
</script>