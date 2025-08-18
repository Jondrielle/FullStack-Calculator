<script setup>
import { ref } from 'vue'
import api from '../services/api.js'

const expression = ref('')
const result = ref(null)

function append(value) {
  if (value === 'AC') {
    expression.value = ''
    result.value = null
  } else if (value === '=') {
    calculate()
  } else {
    expression.value += value
  }
}

async function calculate() {
  if (!expression.value) return

  try {
    const response = await api.post('/calculate', {
      expr: expression.value  // <-- matches backend key
    })

    result.value = response.data.result
    expression.value = result.value  // clear input after calculation
  } catch (error) {
    console.error(error)
    result.value = 'Error'
    expression.value = ''
  }
}
</script>

<template>
  <div style="text-align:center">
    <input v-model="expression" placeholder="0" />

    <div class="numberButtons">
      <button @click="append('AC')">AC</button>
      <button @click="append('/')">/</button>
      <button @click="append('*')">*</button>
      <button @click="append('-')">-</button>

      <button @click="append('7')">7</button>
      <button @click="append('8')">8</button>
      <button @click="append('9')">9</button>
      <button @click="append('+')">+</button>

      <button @click="append('4')">4</button>
      <button @click="append('5')">5</button>
      <button @click="append('6')">6</button>
      <button @click="append('^')">^</button>

      <button @click="append('1')">1</button>
      <button @click="append('2')">2</button>
      <button @click="append('3')">3</button>
      <button @click="append('.')">.</button>

      <button class="zero" @click="append('0')">0</button>
      <button class="equals" @click="append('=')">=</button>
    </div>

    <p v-if="result !== null">Result: {{ result }}</p>
  </div>
</template>

<style>
.numberButtons {
  display: grid;
  grid-template-columns: repeat(4, 60px);
  gap: 10px;
  justify-content: center;
  margin-top: 20px;
}

button {
  padding: 15px;
  border-radius: 8px;
  border: 1px solid #ccc;
  background-color: #f0f0f0;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #d0d0d0;
}

input {
  width: 250px;
  height: 40px;
  font-size: 18px;
  text-align: right;
  margin-bottom: 15px;
  padding: 5px 10px;
}

.zero {
  grid-column: span 2; /* Make zero button wider */
}

.equals {
  grid-column: span 2; /* Make = button wider */
  background-color: #4caf50;
  color: white;
}
.equals:hover {
  background-color: #45a049;
}
</style>
