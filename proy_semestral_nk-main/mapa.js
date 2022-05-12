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
      let marcador = new ol.Feature({
          geometry: new ol.geom.Point(
              ol.proj.fromLonLat([-70.65756761617249,-33.4471033392087])
          ),
      });
      marcador.setStyle(new ol.style.Style({
          image: new ol.style.Icon({
              src: "assets/marcador2.png",
              
          })
      }));
      const marcadores = [];

      marcadores.push(marcador);
      let capa = new ol.layer.Vector({
          source: new ol.source.Vector({
              features: marcadores
          }),
      });
      map.addLayer(capa);
      
      
});

  $("#elemento").width(30);
