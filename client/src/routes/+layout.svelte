<script lang="ts">
	import "../app.css";
	import favicon from '$lib/assets/favicon.svg';
	// import "the-new-css-reset/css/reset.css";

	// Components
	import Header from "$lib/Header.svelte";
	import Footer from "$lib/Footer.svelte";
	
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>
<Header></Header>
{@render children?.()}
<Footer></Footer>
<style>

</style>
