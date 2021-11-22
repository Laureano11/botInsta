from instabot import Bot
import shutil
import time
from tqdm import tqdm

avax= Bot()

##avax.login(username="avax.indumentaria", password="Valija11")




def send_message_all_users(botUse, mensaje):
    for follower in botUse.followers :
        botUse.send_message(mensaje, follower)
    print("Sent An Individual Messages To Your Followers..")
    time.sleep(1)
    exit()


#message = input("Que mensaje desea enviar?")

##send_message_all_users(avax, message)

#print(avax.followers)

def obtenerUsuariosdeId(bot):
    lista=[]
    range= len(bot.followers)
    for i in range:
        lista.append(bot.get_username_from_user_id(bot.followers[i]))
    return lista

#obtenerUsuariosdeId(avax)



##print("enviado como variable ", avax.get_username_from_user_id(48245188681))


numeros= [3,4,54,3234,5,6456,234,43]
print(numeros[3])

##infoId= list(avax.get_user_info(48245188681))
#print(infoId[3])

##mensajes= list(avax.get_messages())
##print(avax.get_messages())
##print("The diference")
##print(mensajes)

#botardo.send_messages(message, botardo.followers)

'viewer', 'inbox', 'seq_id', 'snapshot_at_ms', 'pending_requests_total', 'has_pending_top_requests', 'status'

lista= list({'viewer': {'pk': 50137885539, 'username': 'avax.indumentaria', 'full_name': 'Indumentaria AVAX', 'is_private': False, 'profile_pic_url': 'https://instagram.faep16-2.fna.fbcdn.net/v/t51.2885-19/s150x150/258881588_1287260378457994_3137551620943522946_n.jpg?_nc_ht=instagram.faep16-2.fna.fbcdn.net&_nc_cat=110&_nc_ohc=MR-kGR4D25QAX9kM4AL&edm=AI8ESKwBAAAA&ccb=7-4&oh=ace0af3896de7df27d6d90380272c001&oe=61A284D7&_nc_sid=195af5', 'profile_pic_id': '2710709426614792961_50137885539', 'is_verified': False, 'follow_friction_type': -1, 'has_anonymous_profile_picture': False, 'reel_auto_archive': 'unset', 'is_using_unified_inbox_for_direct': False, 'biz_user_inbox_state': 0, 'wa_addressable': True, 'wa_eligibility': 0, 'interop_messaging_user_fbid': 17851760660669540, 'account_badges': []}, 'inbox': {'threads': [{'thread_id': '340282366841710300949128208331709903196', 'thread_v2_id': '17938493485642076', 'users': [{'pk': 1663108363, 'username': 'nicoburgio19', 'full_name': 'Nicolino Burgio', 'is_private': False, 'profile_pic_url': 'https://instagram.faep16-1.fna.fbcdn.net/v/t51.2885-19/s150x150/117280393_300756220982035_3428200354108028359_n.jpg?_nc_ht=instagram.faep16-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=o_YEFRAhP3wAX8CnJdv&edm=AI8ESKwBAAAA&ccb=7-4&oh=338d2e543d182e34efe0600a4acf420a&oe=61A1D2E8&_nc_sid=195af5', 'profile_pic_id': '2371600069989606972_1663108363', 'friendship_status': {'following': True, 'blocking': False, 'is_private': False, 'incoming_request': False, 'outgoing_request': False, 'is_bestie': False, 'is_restricted': False, 'reachability_status': 0, 'is_feed_favorite': False}, 'is_verified': False, 'follow_friction_type': 0, 'has_anonymous_profile_picture': False, 'has_threads_app': False, 'is_using_unified_inbox_for_direct': False, 'biz_user_inbox_state': 0, 'wa_addressable': True, 'wa_eligibility': 0, 'interop_messaging_user_fbid': 120035066054248, 'account_badges': []}], 'left_users': [], 'admin_user_ids': [], 'items': [{'item_id': '30208446146414162921858242843770880', 'user_id': 1663108363, 'timestamp': 1637603146967680, 'item_type': 'text', 'text': 'Hola', 'client_context': '6868605428590197156', 'show_forward_attribution': False, 'is_shh_mode': False, 'tq_seq_id': 54}], 'last_activity_at': 1637603146967000, 'muted': True, 'is_pin': False, 'named': False, 'canonical': True, 'pending': False, 'archived': False, 'spam': False, 'bc_partnership': False, 'thread_type': 'private', 'viewer_id': 50137885539, 'thread_title': 'nicoburgio19', 'folder': 0, 'system_folder': 0, 'thread_has_drop_in': False, 'thread_has_audio_only_call': False, 'rtc_feature_set_str': None, 'vc_muted': False, 'is_group': False, 'mentions_muted': False, 'approval_required_for_new_members': False, 'input_mode': 0, 'business_thread_folder': 0, 'read_state': 1, 'last_non_sender_item_at': 1637603146967680, 'last_seen_at': {'50137885539': {'timestamp': '1637600282524717', 'item_id': '30208393306767910722579810507292672', 'created_at': '1637600282524717', 'shh_seen_state': {}}}, 'assigned_admin_id': 0, 'shh_mode_enabled': False, 'shh_toggler_userid': None, 'shh_replay_enabled': False, 'is_close_friend_thread': False, 'is_verified_thread': False, 'tq_seq_id': 54, 'uq_seq_id': 81, 'label_items': [], 'is_fanclub_subscriber_thread': False, 'is_translation_enabled': False, 'thread_languages': {}, 'pending_user_ids': [], 'relevancy_score': 1066, 'relevancy_score_expr': 19088687, 'inviter': {'pk': 1663108363, 'username': 'nicoburgio19', 'full_name': 'Nicolino Burgio', 'is_private': False, 'profile_pic_url': 'https://instagram.faep16-1.fna.fbcdn.net/v/t51.2885-19/s150x150/117280393_300756220982035_3428200354108028359_n.jpg?_nc_ht=instagram.faep16-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=o_YEFRAhP3wAX8CnJdv&edm=AI8ESKwBAAAA&ccb=7-4&oh=338d2e543d182e34efe0600a4acf420a&oe=61A1D2E8&_nc_sid=195af5', 'profile_pic_id': '2371600069989606972_1663108363', 'is_verified': False, 'follow_friction_type': 0, 'has_anonymous_profile_picture': False, 'reachability_status': 0, 'account_badges': []}, 'has_older': False, 'has_newer': False, 'newest_cursor': '30208446146414162921858242843770880', 'oldest_cursor': '30208446146414162921858242843770880', 'next_cursor': 'MAXCURSOR', 'prev_cursor': 'MINCURSOR', 'last_permanent_item': {'item_id': '30208446146414162921858242843770880', 'user_id': 1663108363, 'timestamp': 1637603146967680, 'item_type': 'text', 'text': 'Hola', 'client_context': '6868605428590197156', 'show_forward_attribution': False, 'is_shh_mode': False, 'tq_seq_id': 54}, 'has_restricted_user': False, 'has_groups_xac_ineligible_user': False}], 'has_older': False, 'unseen_count': 1, 'unseen_count_ts': 1637603200294490, 'prev_cursor': {'cursor_timestamp_seconds': 0, 'cursor_relevancy_score': 0, 'cursor_thread_v2_id': 0}, 'next_cursor': {'cursor_timestamp_seconds': 18446744073709551615, 'cursor_relevancy_score': 18446744073709551615, 'cursor_thread_v2_id': 18446744073709551615}, 'blended_inbox_enabled': False}, 'seq_id': 81, 'snapshot_at_ms': 1637603200306, 'pending_requests_total': 0, 'has_pending_top_requests': False, 'status': 'ok'}
)
print(lista)


time.sleep(2)
shutil.rmtree("config")