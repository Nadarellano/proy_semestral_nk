$(document).ready(function() {
   
      let map = new ol.Map({
          target: 'map',
          layers: [
            new ol.layer.Tile({
              source: new ol.source.OSM()
            })
          ],
          view: new ol.View({
            center: ol.proj.fromLonLat([-70.71562202641871,-32.73890476596692]),
            zoom: 17
          
          })
          
        });
});
