<script>
	/**
	 * File description:
	 * Provides a component to change the title value of the page.
	 */

	export let title;
</script>

<svelte:head>
	<title>
        {title}
	</title>
</svelte:head>