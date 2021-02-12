function restaurantesZihua()
{
    let slidesZihuaNumber, slidesZihuaToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_restaurantes_zihua')
        .then(response => {
            slidesZihuaNumber = response.data;

            if(slidesZihuaNumber >= 4)
                slidesZihuaToShow = 3;
            else if (slidesZihuaNumber == 3)
                slidesZihuaToShow = 2;
            else if (slidesZihuaNumber == 2)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 1)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }

            console.log('Number of slides restaurantes: ', slidesZihuaNumber);
            console.log('Slides to show restaurantes: ', slidesZihuaToShow);

            $(".slider-restaurantes").slick({
                infinite: true,
                slidesToShow: slidesZihuaToShow,
                slidesToScroll: 1,
                dots: true,
                autoplay: true,
                autoplaySpeed: 5000,
                centerMode: true
            });
        }).catch(e => {
            console.log(e);
        });
    });
}

function lugaresZihua()
{
    let slidesZihuaNumber, slidesZihuaToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_lugares_zihua')
        .then(response => {
            slidesZihuaNumber = response.data;

            if(slidesZihuaNumber >= 4)
                slidesZihuaToShow = 3;
            else if (slidesZihuaNumber == 3)
                slidesZihuaToShow = 2;
            else if (slidesZihuaNumber == 2)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 1)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }

            console.log('Number of slides lugares: ', slidesZihuaNumber);
            console.log('Slides to show lugares: ', slidesZihuaToShow);

            $(".slider-lugares").slick({
                infinite: true,
                slidesToShow: slidesZihuaToShow,
                slidesToScroll: 1,
                dots: true,
                autoplay: true,
                autoplaySpeed: 5000,
                centerMode: true
            });

            $(".slider-acapulco").slick({
                infinite: true,
                slidesToShow: 3,
                slidesToScroll: 1,
                dots: true,
                autoplay: true,
                autoplaySpeed: 5000,
                centerMode: true
            });
        }).catch(e => {
            console.log(e);
        });
    });
}

function parquesZihua()
{
    let slidesZihuaNumber, slidesZihuaToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_parques_zihua')
        .then(response => {
            slidesZihuaNumber = response.data;

            if(slidesZihuaNumber >= 4)
                slidesZihuaToShow = 3;
            else if (slidesZihuaNumber == 3)
                slidesZihuaToShow = 2;
            else if (slidesZihuaNumber == 2)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 1)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }
            
            console.log('Number of slides parques: ', slidesZihuaNumber);
            console.log('Slides to show parques: ', slidesZihuaToShow);

            if(slidesZihuaNumber > 1)
                $(".slider-parques").slick({
                    infinite: true,
                    slidesToShow: slidesZihuaToShow,
                    slidesToScroll: 1,
                    dots: true,
                    autoplay: true,
                    autoplaySpeed: 5000,
                    centerMode: true
                });
        }).catch(e => {
            console.log(e);
        });
    });
}

function tiendasZihua()
{
    let slidesZihuaNumber, slidesZihuaToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_tiendas_zihua')
        .then(response => {
            slidesZihuaNumber = response.data;

            if(slidesZihuaNumber >= 4)
                slidesZihuaToShow = 3;
            else if (slidesZihuaNumber == 3)
                slidesZihuaToShow = 2;
            else if (slidesZihuaNumber == 2)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 1)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }

            console.log('Number of slides tiendas: ', slidesZihuaNumber);
            console.log('Slides to show tiendas: ', slidesZihuaToShow);

            $(".slider-tiendas").slick({
                infinite: true,
                slidesToShow: slidesZihuaToShow,
                slidesToScroll: 1,
                dots: true,
                autoplay: true,
                autoplaySpeed: 5000,
                centerMode: true
            });
        }).catch(e => {
            console.log(e);
        });
    });
}

function serviciosZihua()
{
    let slidesZihuaNumber, slidesZihuaToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_servicios_zihua')
        .then(response => {
            slidesZihuaNumber = response.data;

            if(slidesZihuaNumber >= 4)
                slidesZihuaToShow = 3;
            else if (slidesZihuaNumber == 3)
                slidesZihuaToShow = 2;
            else if (slidesZihuaNumber == 2)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 1)
                slidesZihuaToShow = 1;
            else if(slidesZihuaNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }

            console.log('Number of slides servicios: ', slidesZihuaNumber);
            console.log('Slides to show servicios: ', slidesZihuaToShow);

            $(".slider-servicios").slick({
                infinite: true,
                slidesToShow: slidesZihuaToShow,
                slidesToScroll: 1,
                dots: true,
                autoplay: true,
                autoplaySpeed: 5000,
                centerMode: true
            });
        }).catch(e => {
            console.log(e);
        });
    });
}

let urlZihua, cardZihua, urlAcapulco, cardAcapulco;

function getImageNameAcapulco() {
    $(window).on("load", function() {
        $(".slider-acapulco div span img").click(function() {
            urlAcapulco = $(this).attr("src");
            cardAcapulco = urlAcapulco.split("/").pop();

            console.log('cardAcapulco: ', cardAcapulco);

            axios.post('/visitas_descargas', {
                nombre: cardAcapulco,
                ciudad: 'Acapulco',
                tipo: 'Visita'
            }).then(response => {
                console.log('Tarjeta visitada');
            }).catch(e => {
                console.log(e);
            });

            //alert(card);
        });
    });
}

function downloadAcapulco() {
    axios({
        url: urlAcapulco,
        method: "GET",
        responseType: "blob"
    }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");

        link.href = url;
        link.setAttribute("download", cardAcapulco);

        document.body.appendChild(link);

        link.click();

        axios.post('/visitas_descargas', {
            nombre: cardAcapulco,
            ciudad: 'Acapulco',
            tipo: 'Descarga'
        }).then(response => {
            console.log('Tarjeta descargada');
        }).catch(e => {
            console.log(e);
        });
    });
}

function getImageNameParques()
{
    $(window).on("load", function() {
        $(".slider-parques div span img").click(function() {
            urlZihua = $(this).attr("src");
            console.log('urlZihua: ', urlZihua);

            cardZihua = urlZihua.split("/").pop();
            console.log('cardZihua: ', cardZihua);

            axios.post('/visitas_descargas', {
                nombre: cardZihua,
                ciudad: 'Zihuatanejo',
                tipo: 'Visita'
            }).then(response => {
                console.log('Tarjeta visitada');
            }).catch(e => {
                console.log(e);
            });

            //alert(card);
        });
    });
}

function getImageNameLugares()
{
    $(window).on("load", function() {
        $(".slider-lugares div span img").click(function() {
            urlZihua = $(this).attr("src");
            console.log('urlZihua: ', urlZihua);

            cardZihua = urlZihua.split("/").pop();
            console.log('cardZihua: ', cardZihua);

            axios.post('/visitas_descargas', {
                nombre: cardZihua,
                ciudad: 'Zihuatanejo',
                tipo: 'Visita'
            }).then(response => {
                console.log('Tarjeta visitada');
            }).catch(e => {
                console.log(e);
            });

            //alert(card);
        });
    });
}

function getImageNameRestaurantes()
{
    $(window).on("load", function() {
        $(".slider-restaurantes div span img").click(function() {
            urlZihua = $(this).attr("src");
            console.log('urlZihua: ', urlZihua);

            cardZihua = urlZihua.split("/").pop();
            console.log('cardZihua: ', cardZihua);

            axios.post('/visitas_descargas', {
                nombre: cardZihua,
                ciudad: 'Zihuatanejo',
                tipo: 'Visita'
            }).then(response => {
                console.log('Tarjeta visitada');
            }).catch(e => {
                console.log(e);
            });

            //alert(card);
        });
    });
}

function getImageNameTiendas()
{
    $(window).on("load", function() {
        $(".slider-tiendas div span img").click(function() {
            urlZihua = $(this).attr("src");
            console.log('urlZihua: ', urlZihua);

            cardZihua = urlZihua.split("/").pop();
            console.log('cardZihua: ', cardZihua);

            axios.post('/visitas_descargas', {
                nombre: cardZihua,
                ciudad: 'Zihuatanejo',
                tipo: 'Visita'
            }).then(response => {
                console.log('Tarjeta visitada');
            }).catch(e => {
                console.log(e);
            });

            //alert(card);
        });
    });
}

function getImageNameServicios()
{
    $(window).on("load", function() {
        $(".slider-servicios div span img").click(function() {
            urlZihua = $(this).attr("src");
            console.log('urlZihua: ', urlZihua);

            cardZihua = urlZihua.split("/").pop();
            console.log('cardZihua: ', cardZihua);

            axios.post('/visitas_descargas', {
                nombre: cardZihua,
                ciudad: 'Zihuatanejo',
                tipo: 'Visita'
            }).then(response => {
                console.log('Tarjeta visitada');
            }).catch(e => {
                console.log(e);
            });

            //alert(card);
        });
    });
}

function getImageNameSingle(imgClassRoute)
{
    urlZihua = document.getElementById(imgClassRoute).src;
    console.log('urlZihua: ', urlZihua);

    cardZihua = urlZihua.split("/").pop();
    console.log('cardZihua: ', cardZihua);

    axios.post('/visitas_descargas', {
        nombre: cardZihua,
        ciudad: 'Zihuatanejo',
        tipo: 'Visita'
    }).then(response => {
        console.log('Tarjeta visitada');
    }).catch(e => {
        console.log(e);
    });
}

function downloadZihua() {
    axios({
        url: urlZihua,
        method: "GET",
        responseType: "blob"
    }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");

        link.href = url;
        link.setAttribute("download", cardZihua);

        document.body.appendChild(link);

        link.click();

        axios.post('/visitas_descargas', {
            nombre: cardZihua,
            ciudad: 'Zihuatanejo',
            tipo: 'Descarga'
        }).then(response => {
            console.log('Tarjeta descargada');
        }).catch(e => {
            console.log(e);
        });
    });
}

$(document).ready(function() {
    restaurantesZihua();
    lugaresZihua();
    parquesZihua();
    tiendasZihua();
    serviciosZihua();

    getImageNameLugares();
    getImageNameRestaurantes();
    getImageNameTiendas();
    getImageNameServicios();
    getImageNameAcapulco();
});