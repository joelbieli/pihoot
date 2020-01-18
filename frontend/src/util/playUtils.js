export function getHexForColor(color) {
    const colors = {
        RED: "#FF0000",
        ORANGE: "#FFA500",
        YELLOW: "#FFFF00",
        GREEN: "#32CD32",
        BLUE: "#1E90FF",
        PURPLE: "#9400D3",
        MAGENTA: "#FF00FF"
    };
    switch (color) {
        case 'RED':
            return colors.RED;
        case 'ORANGE':
            return colors.ORANGE;
        case 'YELLOW':
            return colors.YELLOW;
        case 'GREEN':
            return colors.GREEN;
        case 'BLUE':
            return colors.BLUE;
        case 'PURPLE':
            return colors.PURPLE;
        case 'MAGENTA':
            return colors.MAGENTA;
        default:
            console.error('Unknown color!');
    }
}