<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  import io from 'socket.io-client';

  let sensorData = {};
  const socket = io('http://localhost:5000');

  const fetchData = async () => {
      try {
          const response = await axios.get('http://localhost:5000/data');
          sensorData = response.data;
      } catch (error) {
          console.error('Error fetching sensor data:', error);
      }
  };

  onMount(() => {
      fetchData();

      socket.on('data_updated', (data) => {
          sensorData = data.values.reduce((acc, value, index) => {
              acc[index + 1] = value;
              return acc;
          }, {});
      });
  });
</script>

<div class="container">
  <nav class="sidebar">
      <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Services</a></li>
          <li><a href="#">Contact</a></li>
      </ul>
  </nav>
  <main class="content">
      <h1>Welcome to the Simple Sidebar Layout</h1>
      <p>This is a simple example of a sidebar layout using HTML and CSS.</p>
  </main>
</div>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
}

.container {
    display: flex;
}

.sidebar {
    width: 200px;
    background-color: #333;
    color: #fff;
    padding: 15px;
}

.sidebar ul {
    list-style: none;
}

.sidebar ul li {
    margin-bottom: 10px;
}

.sidebar ul li a {
    color: #fff;
    text-decoration: none;
    display: block;
    padding: 10px;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.sidebar ul li a:hover {
    background-color: #575757;
}

.content {
    flex-grow: 1;
    padding: 20px;
}

.content h1 {
    margin-bottom: 20px;
}

.content p {
    line-height: 1.6;
}
</style>
