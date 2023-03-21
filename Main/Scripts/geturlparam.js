function  GetUrlParam(ParamID){
    const urlParams = new URLSearchParams(window.location.search);
    const param = urlParams.get(ParamID);
    return param
}