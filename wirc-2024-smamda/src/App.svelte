<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  import io from 'socket.io-client';

  let sensorData = {};
  let newValue = '';
  const socket = io('http://localhost:5000');

  const fetchData = async () => {
      try {
          const response = await axios.get('http://localhost:5000/data');
          sensorData = response.data;
      } catch (error) {
          console.error('Error fetching sensor data:', error);
      }
  };

  const submitData = async () => {
      try {
          await axios.post('http://localhost:5000/add', { value: parseFloat(newValue) });
          alert('Data updated successfully');
      } catch (error) {
          console.error('Error updating sensor data:', error);
          alert('Failed to update data');
      }
  };

  onMount(() => {
      fetchData();

      socket.on('data_updated', (data) => {
          sensorData = data;
      });
  });
</script>

<main>
<div class="sidebar">
  <img src="..\src\assets\smamda.png" alt="" class="icon" />
  <a class="sidebar-item">Lorem ipsum </a>
  <a class="sidebar-item">Lorem ipsum dolor sit.</a>
</div>
<div class="grid-container">
  <div class="grid-item">{sensorData.value}</div>
  <div class="grid-item">P-2</div>
</div>
</main>

<style>
.icon {
  width: 80%;
  margin-left: 5%;
  margin-bottom: 5%;
}
.sidebar-item {
  display: block;
  background-color: #0e738f;
  color: white;
  font-weight: 600;
  padding: 16px;
  text-decoration: none;
}
.sidebar {
  padding-top: 4%;
  position: fixed;
  background-color: #004e64;
  height: 100%;
  margin-left: 0px;
  width: 10cm;
}
.grid-container {
  margin-top: 2%;
  height: 20%;
  width: 180%;
  align-self: right;
  display: grid;
  grid-template-columns: auto;
  justify-content: space-evenly;
  position: fixed;
}
.grid-item {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 700;
  font-size: xx-large;
  background-color: #535bf200;
  margin-bottom: 20px;
  margin-top: 50px;
  padding-left: 50px;
  padding-top: 80px;
  padding-bottom: 80px;
  border-radius: 10px;
  border-bottom: #0eb1d2 5px solid;
  border-top: #0eb1d2 5px solid;
  border-right: #0eb1d2 5px solid;
  padding-right: 20%;
  width: 10%;
  margin-right: 50rem;
}
</style>
