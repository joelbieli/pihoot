<script>
	import AnswerCorrectIcon from './AnswerCorrectIcon.svelte';
	import {getHexForColor, getTextHexForColor} from '../../../util/playUtils';

	export let answer;
	export let showWhetherAnswerCorrect;
</script>

<style>
	.answer {
		font-weight: bold;
	}
</style>

<div class="uk-width-1-2">
	<div class="uk-card uk-card-default uk-card-small uk-card-body uk-border-rounded"
	     style="{((!showWhetherAnswerCorrect && answer.answer !== '') || (showWhetherAnswerCorrect && answer.answer !== '' && answer.correct)) ? `background-color: ${getHexForColor(answer.color)}` : ''}">
		<div style="height: 10em">
            {#if answer.answer !== ''}
				<div class="uk-grid-small" uk-grid>
					<div class="uk-width-expand">
						<div class="uk-margin-small">
							<h3 class="answer"
							    style="{(showWhetherAnswerCorrect && answer.correct || !showWhetherAnswerCorrect) ? `color: ${getTextHexForColor(answer.color)}` : ''}">
                                {answer.answer}
							</h3>
						</div>
					</div>
					<div class="uk-width-auto">
                        {#if showWhetherAnswerCorrect}
							<AnswerCorrectIcon {answer} {showWhetherAnswerCorrect}/>
                        {/if}
					</div>
				</div>
            {/if}
		</div>
	</div>
</div>