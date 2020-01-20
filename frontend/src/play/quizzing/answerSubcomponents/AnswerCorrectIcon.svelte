<script>
	import {getTextHexForColor} from '../../../util/playUtils';

	export let answer;
	export let showWhetherAnswerCorrect;
</script>

<div>
	<span uk-icon="icon: {answer.correct ? 'check' : 'close'}; ratio: 1.5"
		  style="{!showWhetherAnswerCorrect || (showWhetherAnswerCorrect && answer.correct) ? `color: ${getTextHexForColor(answer.color)}` : ''}"></span>
</div>
