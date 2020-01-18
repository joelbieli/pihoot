export function getHexForColor(color) {
    const colors = {
        RED: "#D01937",
        ORANGE: "#D89D00",
        YELLOW: "#e3e846",
        GREEN: "#25880C",
        BLUE: "#1460BE",
        PURPLE: "#7132B2",
        MAGENTA: "#b324b3"
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

export function getTextHexForColor(color) {
    const colors = {
        WHITE: "#FFF",
        BLACK: "#000"
    };
    switch (color) {
        case 'RED':
            return colors.WHITE;
        case 'ORANGE':
            return colors.WHITE;
        case 'YELLOW':
            return colors.BLACK;
        case 'GREEN':
            return colors.WHITE;
        case 'BLUE':
            return colors.WHITE;
        case 'PURPLE':
            return colors.WHITE;
        case 'MAGENTA':
            return colors.WHITE;
        default:
            console.error('Unknown color!');
    }
}