

var encrypted_supplier

// Global variable - supplier id
var global_supplier_id = document.getElementById('supplier_id').value

// Global variable - delete supplier purchasing info
var delete_supp_purch_data = []

// Global variable - supplier purchasing data
var supplier_org_data = new Array();
$("#display_basic_table TBODY TR").each(function() {
    var row = $(this);
    var save_supp_org_data = {};
    save_supp_org_data.supp_id = global_supplier_id;
    save_supp_org_data.supp_org_guid = row.find("TD").eq(0).text().trim();
    save_supp_org_data.porg_id = row.find("TD").eq(1).text().trim();
    save_supp_org_data.currency_id = row.find("TD").eq(2).text().trim();
    save_supp_org_data.payment_term = row.find("TD").eq(3).text().trim();
    save_supp_org_data.incoterm = row.find("TD").eq(4).text().trim();
    save_supp_org_data.gr_inv_vrf = row.find("TD").eq(5).find('input[type="checkbox"]').is(':checked');
    save_supp_org_data.inv_conf_exp = row.find("TD").eq(6).find('input[type="checkbox"]').is(':checked');
    save_supp_org_data.gr_conf_exp = row.find("TD").eq(7).find('input[type="checkbox"]').is(':checked');
    save_supp_org_data.po_resp = row.find("TD").eq(8).find('input[type="checkbox"]').is(':checked');
    save_supp_org_data.ship_notif_exp = row.find("TD").eq(9).find('input[type="checkbox"]').is(':checked');
    save_supp_org_data.purch_block = row.find("TD").eq(10).find('input[type="checkbox"]').is(':checked');
    supplier_org_data.push(save_supp_org_data)
    console.log(save_supp_org_data)
})


// Makes the supplier basic data fields editable
function edit_basic_supp_data(){
    $('#supplier_basic_update_success').hide();
    $(".hg_edit_display_mode").prop( "disabled", false );
    if(GLOBAL_ACTION != 'CREATE'){
            $("#supplier_id").prop( "disabled", true );
    }
//    $("#currency_id").append(currency_opt1)
//    $("#country_code_id").append(country_opt)
//    $("#language_id").append(language_opt)
    $("#edit_mode").show();
    $("#working_days").hide();
    document.getElementById('sbd_edit_button').style.display = 'none'
    document.getElementById('sbd_save_cancel_button').style.display = 'block'
}

// onclick of cancel button functionality
function cancel_basic_details(){
    $(".hg_edit_display_mode").prop( "disabled", true );
    document.getElementById('sbd_save_cancel_button').style.display = 'none'
    document.getElementById('sbd_edit_button').style.display = 'block'
    $('#image-preview').hide();
    $('#image-preview3').show();
    var output = document.getElementById('image-preview3');
    output.src = img_url;

}

// Function to edit supplier purchasing details data
function edit_supp_org(){
    var supp_org_body_data = '';
// -----------------------------------------------
    $('#display_basic_table').DataTable().destroy();
    $('#supp_org_body').empty();
    var edit_basic_data = '';
    $.each(rendered_supp_org_data, function (i, item) {
         var gr_inv_vrf_checkbox = '';
        if (item.ir_gr_ind){
            gr_inv_vrf_checkbox += '<input type="checkbox"  checked disabled>'
        } else gr_inv_vrf_checkbox += '<input type="checkbox" disabled>'

        var inv_conf_exp_checkbox = '';
        if(item.ir_ind){
            inv_conf_exp_checkbox += '<input type="checkbox"  checked disabled>'
        } else inv_conf_exp_checkbox += '<input type="checkbox" disabled>'

        var gr_conf_exp_checkbox = '';
        if(item.gr_ind){
            gr_conf_exp_checkbox += '<input type="checkbox"  checked disabled>'
        } else gr_conf_exp_checkbox += '<input type="checkbox" disabled>'

        var po_resp_checkbox = '';
        if(item.po_resp){
            po_resp_checkbox += '<input type="checkbox"  checked disabled>'
        } else po_resp_checkbox += '<input type="checkbox" disabled>'

        var ship_notif_exp_checkbox = ''
        if(item.ship_notif_exp){
            ship_notif_exp_checkbox += '<input type="checkbox"  checked disabled>'
        } else ship_notif_exp_checkbox += '<input type="checkbox" disabled>'

        var purch_block_checkbox = ''
        if(item.purch_block){
            purch_block_checkbox += '<input type="checkbox"  checked disabled>'
        } else purch_block_checkbox += '<input type="checkbox" disabled>'

        edit_basic_data += '<tr><td class="class_select_checkbox"><input class="checkbox_check" onclick="valueChanged()" type="checkbox"></td>'+
         '<td hidden>'+item.guid+'</td>'+
         '<td>'+item.porg_id+'</td>'+
         '<td>'+item.currency_id_id+'</td>'+
         '<td>'+item.payment_term_key+'</td>'+
         '<td>'+item.incoterm_key_id+'</td>'+
         '<td>'+gr_inv_vrf_checkbox+'</td>'+
         '<td>'+inv_conf_exp_checkbox+'</td>'+
         '<td>'+gr_conf_exp_checkbox+'</td>'+
         '<td>'+po_resp_checkbox+'</td>'+
         '<td>'+ship_notif_exp_checkbox+'</td>'+
         '<td>'+purch_block_checkbox+'</td></tr>';
    });
    $('#supp_org_body').append(edit_basic_data);
    $("#hg_select_checkbox").prop("hidden", true);
    $("#id_check_all").prop("hidden", false);
    $(".class_select_checkbox").prop("hidden", true);
    $('input:checkbox').removeAttr('checked');
    $('#id_edit_data').show();
    $('#id_cancel_data').hide();
    $('#id_delete_data').hide();
    $('#id_copy_data').hide();
    $('#id_update_data').hide();
    $('#id_save_confirm_popup').modal('hide');
    $('#id_delete_confirm_popup').modal('hide');
//    $('#id_check_all').hide();
    table_sort_filter('display_basic_table');
}

// Function add a new row of supplier purchasing data
function supp_org_add_new_line(){
    add_new_supp_org_data = ''
    add_new_supp_org_data = '<tr><td><input type="checkbox" name="supplier_checkbox"></td> <td hidden></td> <td><select class="form-control"><option selected="true" disabled="disabled"> Select </option>'+porg_opt+'</select></td> <td><select class="form-control"><option selected="true" disabled="disabled"> Select </option>'+ +'</select></td> <td><select class="form-control"><option selected="true" disabled="disabled"> Select </option>'+payterm_opt+'</select></td> <td><select class="form-control"><option selected="true" disabled="disabled"> Select </option>'+incoterm_opt+'</select></td> <td><input type="checkbox"></td> <td><input type="checkbox"></td> <td><input type="checkbox"></td> <td><input type="checkbox"></td> <td><input type="checkbox"></td> <td><input type="checkbox"></td> </tr>'
    $("#supp_org_body").append(add_new_supp_org_data);
}


// Function to cancel Edit operation
function cancel_supp_org_data(){
    display_supp_org_header = ''
    display_supp_org_body = ''
    $('#supp_org_header').empty();
    $('#supp_org_body').empty();

    display_supp_org_header = '<tr> <th>Purchasing organisation</th> <th>PO Currency</th> <th>Payment Terms</th> <th>Incoterm</th> <th>GR based invoice verification</th> <th>Invoice confirmation expected</th> <th>GR confirmation expected</th> <th>PO response</th> <th>Shipping notification expected</th> <th>Purchase block</th></tr>'

    $.each(supplier_org_data, function(index, data){

        var gr_inv_vrf_checkbox = ''
        if (data.gr_inv_vrf==true){
            gr_inv_vrf_checkbox += '<input type="checkbox" checked disabled>'
        } else gr_inv_vrf_checkbox += '<input type="checkbox" disabled>'

        var inv_conf_exp_checkbox = ''
        if(data.inv_conf_exp==true){
            inv_conf_exp_checkbox += '<input type="checkbox" checked disabled>'
        } else inv_conf_exp_checkbox += '<input type="checkbox" disabled>'

        var gr_conf_exp_checkbox = ''
        if(data.gr_conf_exp==true){
            gr_conf_exp_checkbox += '<input type="checkbox" checked disabled>'
        } else gr_conf_exp_checkbox += '<input type="checkbox" disabled>'

        var po_resp_checkbox = ''
        if(data.po_resp==true){
            po_resp_checkbox += '<input type="checkbox" checked disabled>'
        } else po_resp_checkbox += '<input type="checkbox" disabled>'

        var ship_notif_exp_checkbox = ''
        if(data.ship_notif_exp==true){
            ship_notif_exp_checkbox += '<input type="checkbox" checked disabled>'
        } else ship_notif_exp_checkbox += '<input type="checkbox">'

        var purch_block_checkbox = ''
        if(data.purch_block==true){
            purch_block_checkbox += '<input type="checkbox" checked disabled>'
        } else purch_block_checkbox += '<input type="checkbox" disabled>'

        display_supp_org_body += '<tr> <td hidden>'+data.supp_org_guid+'</td> <td>'+data.porg_id+'</td> <td>'+data.currency_id+'</td> <td>'+data.payment_term+'</td> <td>'+data.incoterm+'</td> <td>'+gr_inv_vrf_checkbox+'</td> <td>'+inv_conf_exp_checkbox+'</td> <td>'+gr_conf_exp_checkbox+'</td> <td>'+po_resp_checkbox+'</td> <td>'+ship_notif_exp_checkbox+'</td> <td>'+purch_block_checkbox+'</td></tr> '
    });

    $('#supp_org_header').append(display_supp_org_header);
    $('#supp_org_body').append(display_supp_org_body);
    document.getElementById("id_edit_data").style.display = "block";
//    document.getElementById("supp_org_add_delete_line").style.display = "none";
    document.getElementById("supp_org_cancel_save").style.display = "none";
}


// Function to delete row
function delete_supplier_purch_data() {
    delete_supp_purch_data = []
        del_seq = document.getElementsByName("supplier_checkbox")
        for (index = 0; index < del_seq.length; index++) {
            if (del_seq[index].checked) {
                delete_supp_purch_data.push(del_seq[index].id)
            }
        }
        application_settings_delete_Row('display_basic_table')
        console.log(delete_supp_purch_data)
}


// Function to delete rows from UI
function application_settings_delete_Row(myTable) {
    try {
        var table = document.getElementById(myTable);
        var rowCount = table.rows.length;

        for (var i = 0; i < rowCount; i++) {
            var row = table.rows[i];
            var chkbox = row.cells[0].childNodes[0];
            if (null != chkbox && true == chkbox.checked) {
                table.deleteRow(i);
                rowCount--;
                i--;
            }
        }
        return rowCount;
    } catch (e) {
        alert(e);
    }
}

// Function to save edited supplier basic details data
function save_basic_details() {
    OpenLoaderPopup();
    var name1_val= $('#name1').val();
    var city_val = $('#city_id').val();
    var email_val = $('#email_id').val();
    var mobile_val = $('#mobile_num_id').val();
    var search_term1_val = $('#search_term1_id').val();
    var search_term2_val = $('#search_term2_id').val();
    is_save_form_valid = save_basic_form_validation(name1_val, city_val, email_val, mobile_val, search_term1_val, search_term2_val)
    if (is_save_form_valid != '') {
        $('#save_error_div').html(is_save_form_valid)
        $('#save_error_div').show();
        scroll_top()
        CloseLoaderPopup();
        return
    }

    formdata = new FormData();
    formdata.append("supplier_image",  $('#supplier_image_id').prop('files')[0]);
    formdata.append("supplier_guid",   $('#supplier_guid').val());
    formdata.append("supplier_id",   $('#supplier_id').val()); supplier_type
    formdata.append("supplier_type",   $('#supplier_type').val());
    formdata.append("registration_number",   $('#supplier_regnum').val());
    formdata.append("name1",$('#name1').val());
    formdata.append("name2",$('#name2').val());
    formdata.append("city_id",   $('#city_id').val());
    formdata.append("postal_code_id",   $('#postal_code_id').val());
    formdata.append("street_id",   $('#street_id').val());
    formdata.append("country_code_id",   $('#country_code_id').val());
    formdata.append("currency_id",   $('#currency_id').val());
    formdata.append("language_id",   $('#language_id').val());
    formdata.append("landline_id",   $('#landline_id').val());
    formdata.append("mobile_num_id",   $('#mobile_num_id').val());
    formdata.append("fax_id",   $('#fax_id').val());
    formdata.append("email_id",   $('#email_id').val());
    formdata.append("search_term1_id",   $('#search_term1_id').val());
    formdata.append("search_term2_id",   $('#search_term2_id').val());
    formdata.append("working_days_id",   $('#working_days_id').val());
    formdata.append("duns_number_id",   $('#duns_number_id').val());
    formdata.append("email1_id",   $('#email1_id').val());
    formdata.append("email2_id",   $('#email2_id').val());
    formdata.append("email3_id",   $('#email3_id').val());
    formdata.append("email4_id",   $('#email4_id').val());
    formdata.append("email5_id",   $('#email5_id').val());
    formdata.append("output_medium_id",   $('#output_medium_id').val());
    formdata.append("status",   GLOBAL_ACTION);
    response = ajax_update_supplier_basic_details(formdata)
    console.log(response);
    encrypted_supplier = response.encrypted_supplier
    message = response.message
    // ajax success response
    if(message.success){
        document.getElementById('supplier_basic_update_success').innerHTML = message.success;
        $('#supplier_basic_update_success').show();
        $('#save_error_div').hide();
        CloseLoaderPopup();
    }
    if(message.error){
        document.getElementById('save_error_div').innerHTML = message.error;
        $('#save_error_div').show();
        $('#supplier_basic_update_success').hide();
        CloseLoaderPopup();
    }

    $('html, body').animate({ scrollTop: 0 }, 'slow');
    cancel_basic_details();
    if(GLOBAL_ACTION == 'CREATE'){
        var url = '/admin_tool/supplier_management/supplier_details/' + encrypted_supplier + '';
        location.href = url
    }
    return false;
}
var supplierid = global_supplier_id;
// Function to save edited or updated supplier organizational details data
function supp_org_data_save(){
    OpenLoaderPopup();
    var save_supplier_purch_details = new Array();
    $('#success_msg_id').empty()
    $('#id_popup_table').DataTable().destroy();
    if ((GLOBAL_ACTION == "COPY") || (GLOBAL_ACTION == "ADD")) {
    $("#id_popup_table TBODY TR").each(function() {
        var row = $(this);
        var get_supp_purch_data = {};
        get_supp_purch_data.delete_supplier = delete_supp_purch_data;
        get_supp_purch_data.supp_id = supplierid;
        get_supp_purch_data.supp_org_guid = row.find("TD").eq(1).text();
        get_supp_purch_data.porg_id = row.find("TD").eq(2).find("select option:selected").val();
        get_supp_purch_data.currency_id = row.find("TD").eq(3).find("select option:selected").val();
        get_supp_purch_data.payment_term = row.find("TD").eq(4).find("select option:selected").val();
        get_supp_purch_data.incoterm = row.find("TD").eq(5).find("select option:selected").val();
        get_supp_purch_data.gr_inv_vrf = row.find("TD").eq(6).find('input[type="checkbox"]').is(':checked');
        get_supp_purch_data.inv_conf_exp = row.find("TD").eq(7).find('input[type="checkbox"]').is(':checked');
        get_supp_purch_data.gr_conf_exp = row.find("TD").eq(8).find('input[type="checkbox"]').is(':checked');
        get_supp_purch_data.po_resp = row.find("TD").eq(9).find('input[type="checkbox"]').is(':checked');
        get_supp_purch_data.ship_notif_exp = row.find("TD").eq(10).find('input[type="checkbox"]').is(':checked');
        get_supp_purch_data.purch_block = row.find("TD").eq(11).find('input[type="checkbox"]').is(':checked');
        save_supplier_purch_details.push(get_supp_purch_data)
    })
    $.ajax({
        type: 'POST',
        url: ajax_update_supplier_org_details_url,
        data: JSON.stringify(save_supplier_purch_details),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function (response) {
//            document.getElementById('supplier_org_update_success').innerHTML = response.message;
            success_response(response); // Function call to display response data
//            $('#supplier_org_update_success').show();
            rendered_supp_org_data = response[0];
            edit_supp_org();
//            if (save_supplier_purch_details.length==0){
//                edit_supp_org();
//            } else{
//                supplier_org_data = []
//                for (i = 0; i < save_supplier_purch_details.length; i++){
//                    supplier_org_data.push(save_supplier_purch_details[i])
//                }
//                cancel_supp_org_data();
//                delete_supp_purch_data = []
//            }
            $('#supplierOrgModal').modal('hide');
            CloseLoaderPopup();
        },
        error: function (error) {
            console.log(error);
        }
    })
    }
}
   // Validation function
   const save_basic_form_validation = (name1, city_id, email_id, mobile,search_term1, search_term2) => {
        var is_valid = true
        var save_form_errors = ''
        var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if (name1 == '') {
            is_valid = false

             var msg = "JMSG007" + " First name";
             var msg_type ;
             msg_type = message_config_details(msg);
             $("#error_msg_id").prop("hidden", false)
             var display1 = msg_type.messages_id_desc;
            save_form_errors += display1;
        }
        else if (city_id == '') {
            is_valid = false
              var msg = "JMSG007" + " City";
             var msg_type ;
             msg_type = message_config_details(msg);
             $("#error_msg_id").prop("hidden", false)
             var display1 = msg_type.messages_id_desc;
            save_form_errors += display1 + "City";
        }
        else if ((email_id == '') || !(email_id.match(mailformat))) {
            is_valid = false
              var msg = "JMSG002" + " in Email Id";
             var msg_type ;
             msg_type = message_config_details(msg);
             $("#error_msg_id").prop("hidden", false)
             var display1 = msg_type.messages_id_desc;
            save_form_errors += display1 + "Email Id";
        }
        else if (mobile == '') {
            is_valid = false
              var msg = "JMSG007" + " Mobile Number";
             var msg_type ;
             msg_type = message_config_details(msg);
             $("#error_msg_id").prop("hidden", false)
             var display1 = msg_type.messages_id_desc;
            save_form_errors += display1 + " Mobile Number";
        }
        else if (search_term1 == '') {
            is_valid = false
              var msg = "JMSG007" + " Search Term1";
             var msg_type ;
             msg_type = message_config_details(msg);
             $("#error_msg_id").prop("hidden", false)
             var display1 = msg_type.messages_id_desc;
            save_form_errors += display1 + " Search Term1";
        }
        else if (search_term2 == '') {
            is_valid = false
              var msg = "JMSG007" + " Search Term2";
             var msg_type ;
             msg_type = message_config_details(msg);
             $("#error_msg_id").prop("hidden", false)
             var display1 = msg_type.messages_id_desc;
            save_form_errors += display1 + " Search Term2";
        }

        return is_valid, save_form_errors
    }

function enable_disable(action){
    $(".dummy_ft_button_class").hide();
    if(action == 'EDIT'){
        $("#ft_save").show();
        $("#ft_cancel").show();
        $('.toggle_mode').prop('disabled', false)
    }
    else{
        $("#ft_edit").show();
        $('.toggle_mode').prop('disabled', true)
    }
}


// Function for add a new row data
function new_row_data(){
    basic_add_new_html = '<tr><td><input type="checkbox" required></td>'+
    '<td hidden><input type="text" name="supp_org_guid"></td>'+
    '<td><select class="form-control"  type="text"  name="porg_id" style="text-transform:uppercase;">'+porg_opt+'</select></td>'+
    '<td><select class="form-control" type="text"  name="currency_id">'+currency_opt1+'</select></td>'+
    '<td><select class="form-control" type="text"  name="payment_term">'+payterm_opt+'</select></td>'+
    '<td><select class="form-control" type="text"  name="incoterm">'+incoterm_opt+'</select></td>'+
    '<td><input class="checkbox-size" type="checkbox"  name="gr_inv_vrf_checkbox" required></td>'+
    '<td><input class="checkbox-size" type="checkbox"  name="inv_conf_exp_checkbox" required></td>'+
    '<td><input class="checkbox-size" type="checkbox"  name="gr_conf_exp_checkbox" required></td>'+
    '<td><input class="checkbox-size" type="checkbox"  name="po_resp_checkbox" required></td>'+
    '<td><input class="checkbox-size" type="checkbox"  name="ship_notif_exp_checkbox" required></td>'+
    '<td><input class="checkbox-size" type="checkbox"  name="purch_block_checkbox" required></td>'+
    '<td class="class_del_checkbox" hidden><input type="checkbox" required></td></tr>';
    $('#id_popup_tbody').append(basic_add_new_html);
}
//onclick of cancel display the table in display mode............
function display_basic_db_data() {
    $('#display_basic_table').DataTable().destroy();
    $('#supp_org_body').empty();
    var edit_basic_data = '';
    $.each(rendered_supp_org_data, function (i, item) {
        edit_basic_data += '<tr><td class="class_select_checkbox"><input class="checkbox_check" onclick="valueChanged()" type="checkbox" required></td>'+
        '<td>' + item.porg_id + '</td>'+
        '<td>' + item.currency_id + '</td>'+
        '<td>' + item.payment_term_key + '</td>'+
        '<td>' + item.incoterm_key + '</td>'+
        '<td>' + item.gr_ind + '</td>'+
        '<td>' + item.ir_ind + '</td>'+
        '<td>' + item.ir_gr_ind + '</td>'+
        '<td>' + item.po_resp + '</td>'+
        '<td>' + item.ship_notif_exp + '</td>'+
        '<td>' + item.purch_block + '</td>'+
        '</tr>';
    });
    $('#supp_org_body').append(edit_basic_data);
    $("#hg_select_checkbox").prop("hidden", true);
    $(".class_select_checkbox").prop("hidden", true);
    $('input:checkbox').removeAttr('checked');
    $('#id_edit_data').show();
    $('#id_cancel_data').hide();
    $('#id_delete_data').hide();
    $('#id_copy_data').hide();
    $('#id_update_data').hide();
    $('#id_save_confirm_popup').modal('hide');
    $('#id_delete_confirm_popup').modal('hide');
    $('#id_check_all').hide();
    table_sort_filter('display_basic_table');
}
// Function to get the selected row data
function get_selected_row_data(){
    $("#display_basic_table TBODY TR").each(function () {
        var row = $(this);
        var supp_arr_obj ={};
        supp_arr_obj.del_ind = row.find("TD").eq(0).find('input[type="checkbox"]').is(':checked');
        if(supp_arr_obj.del_ind){
            supp_arr_obj.supp_id = supplierid;
        supp_arr_obj.supp_org_guid = row.find("TD").eq(1).html();
        supp_arr_obj.porg_id = row.find("TD").eq(2).html();
        supp_arr_obj.currency_id = row.find("TD").eq(3).html();
        supp_arr_obj.payment_term = row.find("TD").eq(4).html();
        supp_arr_obj.incoterm = row.find("TD").eq(5).html();
        supp_arr_obj.gr_inv_vrf = row.find("TD").eq(6).find('input[type="checkbox"]').is(':checked');
        supp_arr_obj.inv_conf_exp = row.find("TD").eq(7).find('input[type="checkbox"]').is(':checked');
        supp_arr_obj.gr_conf_exp = row.find("TD").eq(8).find('input[type="checkbox"]').is(':checked');
        supp_arr_obj.po_resp = row.find("TD").eq(9).find('input[type="checkbox"]').is(':checked');
        supp_arr_obj.ship_notif_exp = row.find("TD").eq(10).find('input[type="checkbox"]').is(':checked');
        supp_arr_obj.purch_block = row.find("TD").eq(11).find('input[type="checkbox"]').is(':checked');
            main_table_supp_checked.push(supp_arr_obj);
        }
    });
}

// on click update icon display the selected checkbox data to update
function onclick_update_button() {
    GLOBAL_ACTION = "UPDATE"
    onclick_copy_update_button("UPDATE")
    document.getElementById("id_del_add_button").style.display = "none";
}

// on click add icon display the row in to add the new entries
function add_popup_row() {
    $("#error_msg_id").css("display", "none")
    basic_add_new_html = '';
    var display_db_data = '';
    $('#id_popup_table').DataTable().destroy();
    $(".modal").on("hidden.bs.modal", function () {
        $("#id_error_msg").html(" ");
    });
    new_row_data();   // Add a new row in popup
    if (GLOBAL_ACTION == "country_upload") {
        $(".class_del_checkbox").prop("hidden", false);
        $("#id_del_ind_checkbox").prop("hidden", false);
    }
    table_sort_filter('id_popup_table');
    $('#delete_data').hide()
}
