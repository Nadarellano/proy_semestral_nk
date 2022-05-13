$(document).ready(function() {
   
      let map = new ol.Map({
          target: 'map',
          layers: [
            new ol.layer.Tile({
              source: new ol.source.OSM()
            })
          ],
          view: new ol.View({
            center: ol.proj.fromLonLat([-70.65756761617249,-33.4471033392087]),
            zoom: 17
          
          })
          
        });
});

  
