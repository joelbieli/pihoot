/**
 * File description:
 * Contains utility functions for the play pages.
 */

/**
 * Returns the hex value for a given color string.
 *
 * @global
 *
 * @param {string} color The color name.
 *
 * @return {string} The hex value.
 */
export function getHexForColor(color) {
    const colors = {
        RED: "#D01937",
        YELLOW: "#e3e846",
        GREEN: "#25880C",
        LIGHTBLUE: "#3ab1bb",
        BLUE: "#1460BE",
        PURPLE: "#7132B2"
    };

    switch (color) {
        case 'RED':
            return colors.RED;
        case 'YELLOW':
            return colors.YELLOW;
        case 'GREEN':
            return colors.GREEN;
        case 'LIGHTBLUE':
            return colors.LIGHTBLUE;
        case 'BLUE':
            return colors.BLUE;
        case 'PURPLE':
            return colors.PURPLE;
        default:
            console.error('Unknown color!');
    }
}

/**
 * Returns the hex value for the text color given the color string of the background.
 *
 * @global
 *
 * @param {string} color The background color name.
 *
 * @return {string} The hex value to be applied as a text color.
 */
export function getTextHexForColor(color) {
    const colors = {
        WHITE: "#FFF",
        BLACK: "#000"
    };
    switch (color) {
        case 'RED':
            return colors.WHITE;
        case 'YELLOW':
            return colors.BLACK;
        case 'GREEN':
            return colors.WHITE;
        case 'LIGHTBLUE':
            return colors.WHITE;
        case 'BLUE':
            return colors.WHITE;
        case 'PURPLE':
            return colors.WHITE;
        default:
            console.error('Unknown color!');
    }
}