console.log("eksternal js kebaca")
refresh()
firstTime();
scroll()
function scroll()   {
        $("html, body").animate({scrollTop: "620px" }, 2000);
};
async function refresh()    {
    $.get('/donation/json/', function (data) {
        data.map((donasi) =>
        $('#table-ongoing').append(
            `<tr" class="mylayout" >
                <div class="card mb-3">
                    <div class="card-horizontal">
                        <div class="img-square-wrapper">
                            <img class="photo" src=${imgcard} alt="Card image cap">
                        </div>
                        <div class="row card-body">
                            <div class="col">
                            <h4 class="card-title">Donasi ${donasi.fields.jenis_barang} </h4>
                            <p class="card-text">Banyak (dalam kg): ${donasi.fields.amount}</p>
                            <p class="card-text">Kontak: ${kontak}</p>
                            <p class="card-text">Alamat: ${alamat}</p>
                            <p class="card-text">Shipping method: ${donasi.fields.shipping_method}</p>
                            </div>
                            <div class="card-buttons" style="padding-left:20px; padding-top:20px">
                                <button type="button" name="submit" class="button-selesai" data-id="${donasi.pk}" onclick = "selesai_donasi(${donasi.pk})">Selesai</button>   
                                <button type="button" class="button-selesai" data-bs-toggle="modal" data-bs-target="#myModal${donasi.pk}">Edit</button>        
                            </div>
                            <div class="modal fade" id="myModal${donasi.pk}" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="createTaskModal">Edit Profile</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <form id="modalform" method="post">
                                    
                                    <div class="mb-3">
                                        <label for="donation-jenis" class="col-form-label">Jenis Barang</label>
                                        <input type="text" class="form-control" id="donation-jenis${donasi.pk}" value= "${donasi.fields.jenis_barang}">
                                    </div>
                                    <div class="mb-3">
                                        <label for="donation-amount" class="col-form-label">Banyak (dalam kg)</label>
                                        <input type="number" class="form-control" id="donation-amount${donasi.pk}"" method="post" value= "${donasi.fields.amount}">
                                    </div>
                                    <div class="mb-3">
                                        <label for="donation-ship" class="col-form-label">Shipping method</label>
                                        <select class="form-control"  id="donation-ship${donasi.pk}" method="post">
                                            <option value="${donasi.fields.shipping_method}" selected disabled hidden>${donasi.fields.shipping_method}</option>
                                            <option value="Antar sendiri">Antar sendiri</option>
                                            <option value="JNE">JNE</option>
                                            <option value="POS INDONESIA">POS INDONESIA</option>
                                            <option value="TIKI">TIKI</option>
                                            <option value="SiCepat">SiCepat</option>
                                            <option value="J&T">J&T</option>
                                        </select>
                                    </div>
                                    </form>
                                </div>
                                <div class="modal-footer">
                                <div class="modalbuttons">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" value="Save" name="submit" class ="btn btn-primary" onclick = "edit_donasi(${donasi.pk})"><a >Save</a></button>                                             </div>
                                </div>
                            </div>
                            </div>
                        </div>                      
                        </div>
                    </div>
                    <div class="card-footer">
                        <small class="text-muted historymuted">Last updated on ${donasi.fields.waktu_isi}</small>
                    </div>
                </div>
        </tr>`
        )
        );
    });
    
    $(document).ready(function () {
    $.get('/donation/history/', function (data) {
        data.map((donasi2) =>
        $('#table-history').append(
            `<tr" class="mylayout" >   
                <div class="card mb-3 cardhistory">
                    <div class="card-horizontal">
                        <div class="img-square-wrapper">
                            <img class="photo" src=${imgcard} alt="Card image cap">
                        </div>
                        <div class="card-body">
                            <h4 class="card-title" style="color:#F3F3F3 " >Donasi ${donasi2.fields.jenis_barang} </h4>
                            <p class="card-text">Banyak (dalam kg): ${donasi2.fields.amount}</p>
                            <p class="card-text">Kontak: ${kontak}</p>
                            <p class="card-text">Alamat: ${alamat}</p>
                            <p class="card-text">Shipping method: ${donasi2.fields.shipping_method}</p>                                    
                        </div>
                    </div>
                    <div class="card-footer">
                        <small class="mutedhistory">Last updated on ${donasi2.fields.waktu_isi}</small>
                    </div>
                </div>
        </tr>`
        ))
        
    });
});
}
function edit_donasi(pk2){
    console.log("ini pk2 " + (pk2))
    $("#myModal").modal('show');
    console.log("awal works")
    var linkjenis_barang = "#donation-jenis"+pk2
    var link_amount = "#donation-amount"+pk2
    var link_ship = "#donation-ship"+pk2
    
    var url = "/donation/edit/" + pk2
    const formData = {
        csrfmiddlewaretoken: csrf,
        jenis_barang: $(linkjenis_barang).val(),
        amount: $(link_amount).val(),
        shipping_method: $(link_ship).val(),
    };
    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        success: function(response) {
            alert("Data berhasil diubah!")
            console.log("works")
            $('#table-ongoing').empty()
            refresh()
            $("#modalId").modal('hide'); 
            $('.modal-backdrop').remove();
            $('body').attr("style", "overflow:auto")
        }
        })
        
    }

function selesai_donasi(pk2){
    console.log("awal works")
    console.log("ini pk2: " + pk2)

    var url = "/donation/done/" + pk2
    const formData = {
        csrfmiddlewaretoken: csrf,
    };
    if(confirm("Yakin ingin menyelesaikan donasi?")){
        $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        success: function(response) {
            refresh()
            console.log("works")
            console.log(response.poin)
            $('#table-ongoing').empty()
            $('#table-history').empty()
            $('#linkpoin').html("My points: " + response.poin);
            console.log("berhasil ubah")
            // refresh()
        
        }
        }).done(function (data) {
        alert("selesai donasi!")
        
        });
        };
    }
    
        function firstTime()    {
            var url = "/jsoninfo/"
            const formData = {
                csrfmiddlewaretoken: '{{csrf_token}}'
            };
            {
                $.ajax({
                type: 'POST',
                url: url,
                data: formData,
                success: function(response) {
                    console.log("kebaca")
                    var poin = response.poin
                    var is_auth = response.is_auth
                    console.log(poin)
                    console.log(is_auth)
                    if (is_auth)    {
                    $('#linkpoin').show()
                    $('#linkpoin').html(poin)
                    $('#linkprofile').show()
                    $('#linksignout').html("Sign Out")
                    var oldUrl = $('#linksignout').attr("href")
                    console.log(oldUrl)
                    var newUrl = oldUrl.replace('login-user', 'logout-user')
                    $('#linksignout').attr("href", newUrl)
                    console.log("ada user ga" + is_auth)
                    console.log("poin : " + poin)
                    console.log("berhasil ada user")
                }
                else    {
                    $('#linkprofile').hide()
                    $('#linkpoin').hide()
                    $('#linksignout').html("Sign In")
                    var oldUrl = $('#linksignout').attr("href")
                    var newUrl = oldUrl.replace('logout-user', 'login-user')
                    $('#linksignout').attr("href", newUrl)
                    console.log("berhasil ga ada user")
                }            
                }
                })
                };
        }