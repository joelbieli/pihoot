<script>
	/**
	 * File description:
	 * Provides a text component.
	 */

	export let texts;
</script>

<p>
    {#each texts as text}
        {text}<br>
    {/each}
</p>