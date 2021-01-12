export default function ({ $axios }, inject) {
    function conversion(gridCoord, zoneRestreinte) {
        const originZone = zoneRestreinte[0];
        const finZone = zoneRestreinte[1];
        const intervalGridX = 10;
        const intervalGridY = 10;
        let intervalZoneX = finZone[1] - originZone[1]
        let intervalZoneY = finZone[0] - originZone[0];

        let newCoordX = (gridCoord[0]/intervalGridX) * intervalZoneX
        let newCoordY = (gridCoord[0]/intervalGridY) * intervalZoneY

        return [newCoordX, newCoordY]
    }

    inject("conversion", conversion);

}