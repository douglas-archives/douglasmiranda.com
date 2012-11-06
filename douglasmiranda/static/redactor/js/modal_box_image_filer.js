$(document).ready(function () {
      $('#id_conteudo').getSettings().modal_image = '' +
            '<div id="choose_image_filer_to_redactor" class="redactor_tab">' +
            '    <table class="redactor_ruler" width="100%">' +
            '        <tr>' +
            '            <td nowrap>' +
            '                <img alt="nenhum arquivo selecionado" class="quiet" src="/static/filer/icons/nofile_48x48.png" id="id_filer_insert_image_in_redactor_thumbnail_img">' +
            '            </td>' +
            '            <td width="100%">' +
            '                <span id="id_filer_insert_image_in_redactor_description_txt"></span>' +
            '                <a onclick="return showRelatedObjectLookupPopup(this);" title="Olhar" id="lookup_id_filer_insert_image_in_redactor" class="related-lookup" href="/admin/filer/folder/?t=file_ptr">' +
            '                    <img width="16" height="16" alt="Olhar" src="/static/admin/img/icon_searchbox.png">' +
            '                </a>' +
            '                <img width="10" height="10" style="display: none;" title="Limpar" alt="Limpar" src="/static/admin/img/icon_deletelink.gif" id="id_filer_insert_image_in_redactor_clear">' +
            '                <br>' +
            '                <input type="text" class="span8" name="filer_insert_image_in_redactor" id="id_filer_insert_image_in_redactor" style="display: none;">' +
            '            </td>' +
            '        </tr>' +
            '        <tr>' +
            '            <td nowrap>%__.image_web_link%</td>' +
            '            <td width="100%">' +
            '                <input name="redactor_file_link" id="redactor_file_link"  style="width: 99%"  />' +
            '            </td>' +
            '        </tr>' +
            '        <tr>' +
            '            <td></td>' +
            '            <td>' +
            '                <span class="redactor_btns_box">' +
            '                    <input type="button" name="upload" id="redactor_upload_btn" value="%__.insert%" />&nbsp;&nbsp;' +
            '                    <a href="javascript:void(null);" style="color: #777; font-size: 12px;" id="redactor_btn_modal_close">%__.cancel%</a>' +
            '                </span>' +
            '                <div style="clear: both;"></div> ' +                   
            '                ' +
            '            </td>' +
            '        </tr>' +
            '    </table>' +
            '</div>';
});