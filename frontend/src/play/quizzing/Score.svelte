<script>
	import {getHexForColor, getTextHexForColor} from '../../util/playUtils';

	/**
	 * File description:
	 * Provides a component that displays the score of a single player.
	 */

	// The color that is used to determine background colors and text colors.
	export let color;
	// The color name that is displayed and needed to make the difference between the scoreboard and the leaderboard.
	export let colorName;
	export let score;
	export let position;
</script>

<div class="uk-grid-small uk-border-rounded" uk-grid>
	<div class="uk-width-auto {position < 4 ? 'uk-padding-small' : ''} uk-border-rounded"
	     style="{(position < 4) ? `border-radius: 5px 0 0 5px; background-color: ${getHexForColor(color)};` : ''}">
		<span class="uk-padding-small uk-border-rounded"
		      style="{(position < 4) ? `color: ${getTextHexForColor(color)};` : ''}">
			{position}.
		</span>
	</div>
	<div class="uk-width-expand {position < 4 ? 'uk-padding-small' : ''} uk-border-rounded"
	     style="{(position < 4) ? `border-radius: 0 5px 5px 0; background-color: ${getHexForColor(colorName)};` : ''}">
		<div uk-grid>
			<div class="uk-width-expand">
		<span style="{(position < 4) ? `font-weight: bold; color: ${getTextHexForColor(color)}` : ''}">
			{colorName}
		</span>
			</div>
			<div class="uk-width-auto">
		<span style="{(position < 4) ? `font-weight: bold; color: ${getTextHexForColor(color)}` : ''}">
			{score}
		</span>
			</div>
		</div>
	</div>
</div>