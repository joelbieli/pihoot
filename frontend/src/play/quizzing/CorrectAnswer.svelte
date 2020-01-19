<script>
	export let question;
	export let questionIndex;
	export let questionCount;
</script>

<style>
	.answer {
		font-weight: bold;
	}
</style>

<div class="uk-overlay uk-position-top-left">
    {questionIndex} of {questionCount}
</div>

<TimedLoadingBar seconds="15" barColor="#1e87f0" wrapperColor="#bababa"/>
<div class="uk-grid uk-margin" uk-grid="">
	<div class="uk-width-expand">
		<h1>
            {question.question}
		</h1>
	</div>
	<div class="uk-width-auto">
		<div class="uk-card uk-card-primary uk-card-body uk-border-rounded uk-card-small">
			<h5>
                {countDown}
			</h5>
		</div>
	</div>
</div>
<!-- TODO(laniw): Sort answers by color to be the same as on the answering hardware. -->
<div class="uk-grid-small" uk-grid>
	<div class="uk-width-1-2">
        {#if question.answers[0].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[0].color)}">
				<h3 class="answer" style="color: {getTextHexForColor(question.answers[0].color)}">
                    {question.answers[0].answer}
				</h3>
			</div>
        {:else}
			<div class="uk-card uk-card-default uk-card-small"></div>
        {/if}
	</div>
	<div class="uk-width-1-2">
        {#if question.answers[1].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[1].color)}">
				<h3 class="answer" style="color: {getTextHexForColor(question.answers[1].color)}">
                    {question.answers[1].answer}
				</h3>
			</div>
        {:else}
			<div class="uk-card uk-card-default uk-card-small"></div>
        {/if}
	</div>
	<div class="uk-width-1-2">
        {#if question.answers[2].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[2].color)}">
				<h3 class="answer" style="color: {getTextHexForColor(question.answers[2].color)}">
                    {question.answers[2].answer}
				</h3>
			</div>
        {:else}
			<div class="uk-card uk-card-default uk-card-small"></div>
        {/if}
	</div>
	<div class="uk-width-1-2">
        {#if question.answers[3].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[3].color)}">
				<h3 class="answer" style="color: {getTextHexForColor(question.answers[3].color)}">
                    {question.answers[3].answer}
				</h3>
			</div>
        {:else}
			<div class="uk-card uk-card-default uk-card-small"></div>
        {/if}
	</div>
</div>