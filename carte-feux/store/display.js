export const state = () => ({
    displayCapteur: true,
    displayCaserne: true,
    displayCamion: true
})

export const getters = {
    getDisplayCapteur: state => state.displayCapteur 
}