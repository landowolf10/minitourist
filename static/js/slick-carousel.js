/*************************** ZIHUA ***************************/
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

            if(slidesZihuaNumber >= 1)
                $(".slider-lugares").slick({
                    infinite: true,
                    slidesToShow: slidesZihuaToShow,
                    slidesToScroll: 1,
                    dots: true,
                    autoplay: true,
                    autoplaySpeed: 5000,
                    centerMode: true
                });

            /*$(".slider-acapulco").slick({
                infinite: true,
                slidesToShow: 3,
                slidesToScroll: 1,
                dots: true,
                autoplay: true,
                autoplaySpeed: 5000,
                centerMode: true
            });*/
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

            if(slidesZihuaNumber >= 1)
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

            if(slidesZihuaNumber >= 1)
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

            if(slidesZihuaNumber >= 1)
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

let urlZihua, cardZihua;

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
/*************************** END ZIHUA ***************************/

/*************************** ACAPULCO ***************************/
function lugaresAcapulco()
{
    let slidesAcapulcoNumber, slidesAcapulcoToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_lugares_acapulco')
        .then(response => {
            slidesAcapulcoNumber = response.data;

            if(slidesAcapulcoNumber >= 4)
                slidesAcapulcoToShow = 3;
            else if (slidesAcapulcoNumber == 3)
                slidesAcapulcoToShow = 2;
            else if (slidesAcapulcoNumber == 2)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 1)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }
            
            console.log('Number of slides parques: ', slidesAcapulcoNumber);
            console.log('Slides to show parques: ', slidesAcapulcoToShow);

            if(slidesAcapulcoNumber >= 1)
                $(".slider-lugares-acapulco").slick({
                    infinite: true,
                    slidesToShow: slidesAcapulcoToShow,
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

function restaurantesAcapulco()
{
    let slidesAcapulcoNumber, slidesAcapulcoToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_restaurantes_acapulco')
        .then(response => {
            slidesAcapulcoNumber = response.data;

            if(slidesAcapulcoNumber >= 4)
                slidesAcapulcoToShow = 3;
            else if (slidesAcapulcoNumber == 3)
                slidesAcapulcoToShow = 2;
            else if (slidesAcapulcoNumber == 2)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 1)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }
            
            console.log('Number of slides parques: ', slidesAcapulcoNumber);
            console.log('Slides to show parques: ', slidesAcapulcoToShow);

            if(slidesAcapulcoNumber >= 1)
                $(".slider-restaurantes-acapulco").slick({
                    infinite: true,
                    slidesToShow: slidesAcapulcoToShow,
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

function parquesAcapulco()
{
    let slidesAcapulcoNumber, slidesAcapulcoToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_parques_acapulco')
        .then(response => {
            slidesAcapulcoNumber = response.data;

            if(slidesAcapulcoNumber >= 4)
                slidesAcapulcoToShow = 3;
            else if (slidesAcapulcoNumber == 3)
                slidesAcapulcoToShow = 2;
            else if (slidesAcapulcoNumber == 2)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 1)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }
            
            console.log('Number of slides parques: ', slidesAcapulcoNumber);
            console.log('Slides to show parques: ', slidesAcapulcoToShow);

            if(slidesAcapulcoNumber >= 1)
                $(".slider-parques-acapulco").slick({
                    infinite: true,
                    slidesToShow: slidesAcapulcoToShow,
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

function tiendasAcapulco()
{
    let slidesAcapulcoNumber, slidesAcapulcoToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_tiendas_acapulco')
        .then(response => {
            slidesAcapulcoNumber = response.data;

            if(slidesAcapulcoNumber >= 4)
                slidesAcapulcoToShow = 3;
            else if (slidesAcapulcoNumber == 3)
                slidesAcapulcoToShow = 2;
            else if (slidesAcapulcoNumber == 2)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 1)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }
            
            console.log('Number of slides parques: ', slidesAcapulcoNumber);
            console.log('Slides to show parques: ', slidesAcapulcoToShow);

            if(slidesAcapulcoNumber >= 1)
                $(".slider-tiendas-acapulco").slick({
                    infinite: true,
                    slidesToShow: slidesAcapulcoToShow,
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

function serviciosAcapulco()
{
    let slidesAcapulcoNumber, slidesAcapulcoToShow = 0;

    $(document).ready(function() {
        axios.get('/tarjetas_servicios_acapulco')
        .then(response => {
            slidesAcapulcoNumber = response.data;

            if(slidesAcapulcoNumber >= 4)
                slidesAcapulcoToShow = 3;
            else if (slidesAcapulcoNumber == 3)
                slidesAcapulcoToShow = 2;
            else if (slidesAcapulcoNumber == 2)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 1)
                slidesAcapulcoToShow = 1;
            else if(slidesAcapulcoNumber == 0)
            {
                console.log('No hay usuarios registrados');
                //document.getElementById('slider-zihua').innerHTML = 'No hay usuarios registrados';
            }
            
            console.log('Number of slides parques: ', slidesAcapulcoNumber);
            console.log('Slides to show parques: ', slidesAcapulcoToShow);

            if(slidesAcapulcoNumber >= 1)
                $(".slider-servicios-acapulco").slick({
                    infinite: true,
                    slidesToShow: slidesAcapulcoToShow,
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

let urlAcapulco, cardAcapulco;

function getImageNameParquesAcapulco() {
    $(window).on("load", function() {
        $(".slider-parques-acapulco div span img").click(function() {
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

function getImageNameLugaresAcapulco() {
    $(window).on("load", function() {
        $(".slider-lugares-acapulco div span img").click(function() {
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

function getImageNameRestaurantesAcapulco() {
    $(window).on("load", function() {
        $(".slider-restaurantes-acapulco div span img").click(function() {
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

function getImageNameTiendasAcapulco() {
    $(window).on("load", function() {
        $(".slider-tiendas-acapulco div span img").click(function() {
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

function getImageNameServiciosAcapulco() {
    $(window).on("load", function() {
        $(".slider-servicios-acapulco div span img").click(function() {
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
/*************************** END ACAPULCO ***************************/

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

function getImageNameSingleAcapulco(imgClassRoute)
{
    urlAcapulco = document.getElementById(imgClassRoute).src;
    console.log('urlAcapulco: ', urlAcapulco);

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

$(document).ready(function() {
    restaurantesZihua();
    lugaresZihua();
    parquesZihua();
    tiendasZihua();
    serviciosZihua();
    restaurantesAcapulco();
    lugaresAcapulco();
    parquesAcapulco();
    tiendasAcapulco();
    serviciosAcapulco();

    getImageNameLugares();
    getImageNameRestaurantes();
    getImageNameParques();
    getImageNameTiendas();
    getImageNameServicios();
    getImageNameLugaresAcapulco();
    getImageNameRestaurantesAcapulco();
    getImageNameParquesAcapulco();
    getImageNameTiendasAcapulco();
    getImageNameServiciosAcapulco();
});