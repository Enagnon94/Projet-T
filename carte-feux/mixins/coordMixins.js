export default {
    methods: {
        conversion(gridCoord, zoneRestreinte) {
            const originZone = zoneRestreinte[0];
            const finZone = zoneRestreinte[1];
            const intervalGridX = 6;
            const intervalGridY = 10;
            let intervalZoneX = finZone[0] - originZone[0]
            let intervalZoneY = finZone[1] - originZone[1];
    
            let newCoordX = originZone[0] + (gridCoord[0]/intervalGridX) * intervalZoneX
            let newCoordY = originZone[1] + (gridCoord[1]/intervalGridY) * intervalZoneY
    
            return [newCoordX, newCoordY]
        }
    }
}