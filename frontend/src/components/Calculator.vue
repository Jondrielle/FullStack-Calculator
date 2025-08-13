<script setup>
import { ref } from 'vue'
import api from '../services/api.js'

const result = ref(null)
const expression = ref('')

async function addData() {
  try {
    const response = await api.post('/add', { x: 5, y: 3 })
    result.value = response.data
  } catch (error) {
    console.error('Error:', error)
  }
}

function append(char){
	expression.value += char
}
</script>

<template>
	<div>
		<input v-model="expression" placeholder="0" />
		<div class = "numberButtons">
		  	<div>
			    <button @click="append('1')">1</button>
			    <button @click="append('2')">2</button>
			    <button @click="append('3')">3</button>
			    <button @click="append('+')">+</button>
		  	</div>
			<div>
				<button @click="append('4')">4</button>
			    <button @click="append('5')">5</button>
			    <button @click="append('6')">6</button>
			    <button @click="append('-')">-</button>
			</div>
	  
	    	<div>
			    <button @click="append('7')">7</button>
			    <button @click="append('8')">8</button>
			    <button @click="append('9')">9</button>
			    <button @click="append('*')">*</button>
		  	</div>
	  
		  	<div>
		    	<button @click="append('0')">0</button>
		    	<button @click="append('^')">^</button>
		    </div>
		</div>
  </div>
    <button>Calculate</button>
    <p v-if="result !== null">Result: {{ result }}</p>

</template>


<style>
input{
	border-radius: 50px; 
	border-color: lightgray;
}
.numberButtons{
	border-radius: 10000px;	
	width: 300px;
}
</style>
