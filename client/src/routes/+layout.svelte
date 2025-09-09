<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import "the-new-css-reset/css/reset.css";
	import "../styles/app.css"

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>
<header></header>
{@render children?.()}

<style>

</style>