<script>
	export let texts;
</script>

<p>
    {#each texts as text}
        {text}<br>
    {/each}
</p>