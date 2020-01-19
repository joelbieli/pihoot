<script>
	import {getHexForColor, getTextHexForColor} from '../../util/playUtils'

	export let color;
	export let score;
	export let position;

	function fontBoldRule() {

	}

</script>

<div class="uk-grid-small {position < 4 ? 'uk-padding-small' : ''} uk-border-rounded"
     style="{(position < 4) ? `background-color: ${getHexForColor(color)}` : ''}" uk-grid>
	<div class="uk-width-auto">
		<span style="{(position < 4) ? `color: ${getTextHexForColor(color)}` : ''}">
			{position}.
		</span>
	</div>
	<div class="uk-width-expand">
		<span style="{(position < 4) ? `font-weight: bold; color: ${getTextHexForColor(color)}` : ''}">
			{color}
		</span>
	</div>
	<div class="uk-width-auto">
		<span style="{(position < 4) ? `font-weight: bold; color: ${getTextHexForColor(color)}` : ''}">
			{score}
		</span>
	</div>
</div>