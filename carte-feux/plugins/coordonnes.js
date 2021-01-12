export default function ({ $axios }, inject) {
    function conversion(gridCoord, zoneRestreinte) {
        const originZone = zoneRestreinte[0];
        const finZone = zoneRestreinte[1];
        const intervalGridX = 10;
        const intervalGridY = 10;
        let intervalZoneX = finZone[0] - originZone[0]
        let intervalZoneY = finZone[1] - originZone[1];
        console.log("gridCoor");console.log(gridCoord[1]);console.log("/gridCoor");
        console.log(intervalZoneY);

        let newCoordX = originZone[0] + (gridCoord[0]/intervalGridX) * intervalZoneX
        let newCoordY = originZone[1] + (gridCoord[1]/intervalGridY) * intervalZoneY

        return [newCoordX, newCoordY]
    }

    inject("conversion", conversion);

}