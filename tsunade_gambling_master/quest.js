var kepla_flag = "KKSI2019{",
    place_flag = "Tr0ll1ng_th3_Us3r",
    penutup = "}";

function get_point_now() {
    var t = $("#point").text();
    return parseInt(t)
}

function generate_judi_server(t) {
    return Math.round(Math.random() * t)
}

function genertae_judi_client() {
    return batas = generate_judi_server(100), Math.round(Math.random() * batas)
}

function ready_to_serve() {
    return place_flag.split("_")
}

function serve(t) {
    var e = t;
    for ($i = 0; $i < e.length; $i++) $("#flag" + $i).html("<img src='./fl4g/" + e[$i] + ".png'>")
}
$(document).on("click", "#adu", () => {
    var t = genertae_judi_client(),
        e = generate_judi_server(100);

    $("#client").text(t), $("#server").text(e);
    
    var n = get_point_now();
    
    t > e ? $("#point").text(n + 1) : $("#point").text(n - 1)
}), $(document).on("click", "#judii", () => {
    if (get_point_now() >= 133333333337){
      (console.log("I know you inspect element it!"), $("#flag").text(place_flag + " Don't Submit it Bratan! It's wrong one!"));
    }
    else {
      $("#flag").text("Go Away. Hus Hus");
    }
});