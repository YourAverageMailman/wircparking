<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import io from "socket.io-client";

  let sensorData = {};
  const socket = io("http://localhost:5000");

  const fetchData = async () => {
    try {
      const response = await axios.get("http://localhost:5000/data");
      sensorData = response.data;
    } catch (error) {
      console.error("Error fetching sensor data:", error);
    }
  };

  onMount(() => {
    fetchData();

    socket.on("data_updated", (data) => {
      sensorData = data.values.reduce((acc, value, index) => {
        acc[index + 1] = value;
        return acc;
      }, {});
    });
  });

  let isOpen = false;

  function toggleDropdown() {
    isOpen = !isOpen;
  }

  function closeDropdown() {
    isOpen = false;
  }
</script>

<nav>
  <img
    id="icon"
    class="nav-item"
    src="https://play-lh.googleusercontent.com/2x2QYh3UlhBp5CYl63N2nP0eX3TSbikRFh38WUuh7oToWGamdXkPz5wrwOmDK-7GSg=w240-h480-rw"
    alt=""
  />

  <div class="dropdown nav-item" on:blur={closeDropdown}>
    <button class="dropdown-button" on:click={toggleDropdown}>Members</button>
    <div class="dropdown-content {isOpen ? 'show' : ''}">
      <a href="#option1">Rezvan</a>
      <a href="#option2">Aurellino</a>
      <a href="#option3">Fahri</a>
    </div>
  </div>
</nav>
<main class="flex-container">
  <div class="flex-item">
    <h1 class="parking-header">1st Floor</h1>
    <div class="parking-space">
      <div class={sensorData[1] ? 'parking-full' : 'parking-empty'}>
        {#if sensorData[1]}
          <img
            src="https://cdn.discordapp.com/attachments/902905746528829460/1257254959741665290/car-icon.png?ex=6683bd6d&is=66826bed&hm=1961c7949252db8c605f25e1a7b8bb9b818e5beeaacd483459c52f9324cdf277&"
            alt=""
            class="parking-icon"
          />
        {:else}
          <h2>EMPTY</h2>
        {/if}
      </div>
      <div class={sensorData[2] ? 'parking-full' : 'parking-empty'}>
        {#if sensorData[2]}
          <img
            src="https://cdn.discordapp.com/attachments/902905746528829460/1257254959741665290/car-icon.png?ex=6683bd6d&is=66826bed&hm=1961c7949252db8c605f25e1a7b8bb9b818e5beeaacd483459c52f9324cdf277&"
            alt=""
            class="parking-icon"
          />
        {:else}
          <h2>EMPTY</h2>
        {/if}
      </div>
      <div class={sensorData[3] ? 'parking-full' : 'parking-empty'}>
        {#if sensorData[3]}
          <img
            src="https://cdn.discordapp.com/attachments/902905746528829460/1257254959741665290/car-icon.png?ex=6683bd6d&is=66826bed&hm=1961c7949252db8c605f25e1a7b8bb9b818e5beeaacd483459c52f9324cdf277&"
            alt=""
            class="parking-icon"
          />
        {:else}
          <h2>EMPTY</h2>
        {/if}
      </div>
    </div>
  </div>
  <div class="flex-item">
    <h1 class="parking-header">2nd Floor</h1>
    <div class="parking-space">
      <div class={sensorData[4] ? 'parking-full' : 'parking-empty'}>
        {#if sensorData[4]}
          <img
            src="https://cdn.discordapp.com/attachments/902905746528829460/1257254959741665290/car-icon.png?ex=6683bd6d&is=66826bed&hm=1961c7949252db8c605f25e1a7b8bb9b818e5beeaacd483459c52f9324cdf277&"
            alt=""
            class="parking-icon"
          />
        {:else}
          <h2>EMPTY</h2>
        {/if}
      </div>
      <div class={sensorData[5] ? 'parking-full' : 'parking-empty'}>
        {#if sensorData[5]}
          <img
            src="https://cdn.discordapp.com/attachments/902905746528829460/1257254959741665290/car-icon.png?ex=6683bd6d&is=66826bed&hm=1961c7949252db8c605f25e1a7b8bb9b818e5beeaacd483459c52f9324cdf277&"
            alt=""
            class="parking-icon"
          />
        {:else}
          <h2>EMPTY</h2>
        {/if}
      </div>
      <div class={sensorData[6] ? 'parking-full' : 'parking-empty'}>
        {#if sensorData[6]}
          <img
            src="https://cdn.discordapp.com/attachments/902905746528829460/1257254959741665290/car-icon.png?ex=6683bd6d&is=66826bed&hm=1961c7949252db8c605f25e1a7b8bb9b818e5beeaacd483459c52f9324cdf277&"
            alt=""
            class="parking-icon"
          />
        {:else}
          <h2>EMPTY</h2>
        {/if}
      </div>
  </div>
</main>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Red+Hat+Display:ital,wght@0,300..900;1,300..900&display=swap");

  #icon {
    height: 6rem;
    margin-right: 2rem;
  }
  :root {
    --background: #1c1f26;
    --background-2: #2d323e;
    --foreground: #1b41b3;
    --foreground-2: #265dff;
    --text-fg: #1c1f26;
    --text-bg: #ebf5ff;
    background-color: var(--background);
    font-family: "Red Hat Display", sans-serif;
    color: white;
  }
  nav {
    font-size: x-large;
    padding: 0.5rem;
    background-color: var(--foreground);
    margin: 0px;
    color: #292f36;
    font-weight: 800;
    display: flex;
    justify-content: space-between;
    position: relative;
    padding-top: 0.8rem;
  }

  .nav-item {
    margin-right: 0.2rem;
  }
  .flex-container {
    display: flex;
  }
  .flex-item {
    width: 100%;
    height: 100%;
  }
  .parking-header {
    margin: 1.5rem;
    color: var(--text-bg);
    background-color: var(--background-2);
    padding: 1.5rem;
    border-radius: 5px;
  }
  .parking-space {
    background-color: var(--background);
    display: grid;
  }
  .parking-full {
    text-align: center;
    padding: 0.5rem;
    margin-left: auto;
    margin-right: auto;
	margin-top: 10px;
    border-top: red solid 10px;
    border-right: red solid 15px;
    border-bottom: red solid 10px;
    border-radius: 15px;
	  width: 100px;
	  height: 50px;
  }
  .parking-empty {
    text-align: center;
    padding: 0.5rem;
    margin-left: auto;
    margin-right: auto;
	margin-top: 10px;
    border-top: green solid 10px;
    border-right: green solid 15px;
    border-bottom: green solid 10px;
    border-radius: 15px;
	  width: 100px;
	  height: 50px;
  }
  .parking-icon {
    width: 100px;
    height:auto;
  }
  /* @media (max-width: 480px) {
		#user {
			height: auto;
			line-height: normal;
			padding: 1rem;
			margin-top: 1rem;
			white-space: normal;
			width: 100%;
			text-align: center;
		}
		.parking {
			margin-left: 10%;
			margin-right: 10%;
		}
	} */

  .dropdown {
    position: relative;
    display: inline-block;
    align-items: center;
    justify-self: flex-end !important;
  }

  .dropdown-content {
    display: none;
    position: absolute;
    background-color: var(--foreground);
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
    border-radius: 8px;
  }

  .dropdown-content a {
    color: var(--text-bg);
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    border-radius: 8px;
    transition-property: background-color transform box-shadow;
    transition-duration: 100ms;
    transition-timing-function: cubic-bezier(0.445, 0.05, 0.55, 0.95);
  }

  .dropdown-content a:hover {
    background-color: var(--foreground-2);
    transform: scale(110%) translateY(-5px);
    box-shadow: 2px 2px 2px #020c2a;
  }

  .dropdown-content.show {
    display: block;
  }

  .dropdown-button {
    height: 100%;
    background-color: var(--foreground-2);
    padding: 1.5rem;
    font-size: x-large;
    border: none;
    cursor: pointer;
    text-align: center;
    border-radius: 8px;
    font-weight: 900;
    color: var(--text-bg);
    transition-property: transform box-shadow;
    transition-duration: 100ms;
    transition-timing-function: cubic-bezier(0.445, 0.05, 0.55, 0.95);
  }

  .dropdown-button:hover {
    transform: scale(110%) translateY(-5px);
    box-shadow: 2px 2px 2px #020c2a;
  }
</style>
