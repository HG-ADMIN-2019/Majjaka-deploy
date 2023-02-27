$(document).ready(function () {
    $('#nav_menu_items').remove();
    $("body").css("padding-top", "3.7rem");
    table_sort_filter('display_basic_table');
});
var currPageStartIdx, currPageEndIdx;
//var table = $('#display_basic_table').DataTable();
// on click edit icon display the data in edit mode
function onclick_edit_button() {
    //display the add,cancel and upload buttons and select all checkbox,select heading and checkboxes for each row
    $('#display_basic_table').DataTable().destroy();
    $("#hg_select_checkbox").prop("hidden", false);
    $(".class_select_checkbox").prop("hidden", false);

    //hide the edit,delete,copy and update buttons
    $('#id_cancel_data').show();
    $('#id_edit_data').hide();
    $('#id_check_all').show();
    table_sort_filter('display_basic_table');
}

//onclick of select all checkbox
function checkAll(ele) {
    $('#display_basic_table').DataTable().destroy();
    var checkboxes = document.getElementsByTagName('input');
    if (ele.checked) {
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].type == 'checkbox') {
                checkboxes[i].checked = true;
                $('#id_delete_data').show();
                $('#id_copy_data').show();
                $('#id_update_data').show();
            }
        }
    } else {
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].type == 'checkbox') {
                checkboxes[i].checked = false;
                $('#id_delete_data').hide();
                $('#id_copy_data').hide();
                $('#id_update_data').hide();
            }
        }
    }
    table_sort_filter('display_basic_table');
}

//onclick of checkbox display delete,update and copy Buttons
function valueChanged() {
    if ($('.checkbox_check').is(":checked")) {
        $('#id_delete_data').show();
        $('#id_copy_data').show();
        $('#id_update_data').show();
    } else {
        $('#id_delete_data').hide();
        $('#id_copy_data').hide();
        $('#id_update_data').hide();
    }
}

//onclick of delete,delete the row.
function application_settings_delete_Row(myTable) {
    $('#id_popup_table').DataTable().destroy();
    var uncheck_count=0

     try {
        $("#id_popup_table TBODY TR").each(function() {
            var row = $(this);
            var checked = row.find("TD").eq(0).find('input[type="checkbox"]').is(':checked')
            if (!(row.find("TD").eq(0).find('input[type="checkbox"]').is(':checked'))){
                uncheck_count ++;
            }
        });
        if (uncheck_count==0){
            $('#myModal').modal('hide');
            $('#delete_not_possible').modal('show');
        }
        else{
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
            $("#id_delete_currency").hide();
            $("#id_copy_currency").hide();
            $("#id_update_currency").hide();
            $("#error_msg_id").css("display", "none");
            table_sort_filter_popup('id_popup_table');
            return rowCount;
        }

    } catch (e) {
        alert(e);
    }
}


function display_popup(){
    $('#delete_not_possible').modal('hide');
    $('#myModal').modal('show');

}

// Function to display Description based on element Id
function display_message(id, description){
                $('#'+id).html(description);
                $('#'+id).css("display", "block");
                $('#id_save_confirm_popup').modal('hide');
                $('#myModal').modal('show');

}

//// Function to hide and display save related popups
//$('#save_id').click(function () {
//    $('#myModal').modal('hide');
//    $('#id_save_confirm_popup').modal('show');
//});

function get_message_details(msgId){
    var msg_type ;
    msg_type = message_config_details(msgId);
    $("#error_msg_id").prop("hidden", false);
    if(msg_type.message_type == "ERROR"){
        display_message("error_msg_id", msg_type.messages_id_desc)
    }
    else if(msg_type.message_type == "WARNING"){
     display_message("id_warning_msg_id", msg_type.messages_id_desc)
    }
    else if(msg_type.message_type == "INFORMATION"){
     display_message("id_info_msg_id", msg_type.messages_id_desc)
    }
}

// Function for close window button
function window_close() {
     window.history.back();
      var preUrl = document.referrer;
      window.open('', '_self', '').close();
      if (preUrl == null)
             return "The previous page url is empty";
     else
             return preUrl;
}
// Success response function
function success_response(Response){
     $('#success_msg_id').text(Response[1])
      if(Response[1].message_type== 'SUCCESS'){
         $('#success_msg_id').text(Response[1].message_desc)
      }
    $("#err_msg_app_settings_t").prop("hidden", false)
    table_sort_filter('id_popup_table');
     // function to display success msg based on sys setting msg interval time
    message_display_time();
}
// Function to hide the error message in data upload pop up
function cancel_upload(){
    $("#id_error_msg_upload").prop("hidden",true);
    $('#id_data_upload').modal('hide');
}
function display_file_select_error(){
    $("#id_error_msg_upload").prop("hidden",false);
    var msg = "JMSG110";
    var msg_type ;
    msg_type = message_config_details(msg);
    get_message_details(msg); // Get message details
    var display = msg_type.messages_id_desc;
    document.getElementById("id_error_msg_upload").innerHTML = display;
    document.getElementById("id_error_msg_upload").style.color = "Red";
    $('#id_data_upload').modal('show');
}