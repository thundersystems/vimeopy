Client
======

Configuration
+++++++++++++

A client instance use a configuration dict where you can configure::

    _initial_client_configuration = {
        'API_ROOT': 'https://api.vimeo.com',
        'HTTP_METHODS': {'head', 'get', 'post', 'put', 'patch', 'options', 'delete'},  # set
        'ACCEPT_HEADER': "application/vnd.vimeo.*;version=3.2",
        'USER_AGENT': "pyvimeo 0.1; (http://developer.vimeo.com/api/docs)",
        'TIMEOUT': (1, 30),
    }


Singleton
+++++++++

In Vimeopy a singleton client is available, the use is identical to VimeoClient with the difference that it is only
instantiated the first time::

    from vimeo.clients import VimeoClientSingleton
    vimeo_client = VimeoClientSingleton(token='YOUR_APP_TOKEN')


Methods
+++++++

read_user
---------

.. py:function:: read_user()

   Return *response* that contain a json that describe current user

   :return: current user
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.

update_user
-----------

.. py:function:: update_user(data)

   Return *response* that contain a json that describe the user after *data* changes are applied.

   :param dict list_id: Dict of the changes to be applied to the user, not all items are required but only items of change.
   :return: current user
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


create_album
------------

.. py:function:: create_album(name, description, privacy=None, password=None, sort=None)

   Return *response* that contain a json that describe album created
   Note that you must have a create scope enabled to perform this operation

   :return: album
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.



read_albums
-----------

.. py:function:: read_albums()

   Return *response* that contain a json that describe all albums.

   :return: albums
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_album
----------

.. py:function:: read_album(album_id)

   Return *response* that contain a json that describe album with *album_id* id

   :param int album_id: id of album to retrieve.
   :return: album
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_album_videos
-----------------

.. py:function:: read_album_videos(album_id)

   Return *response* that contain a json that describe all videos in album

   :param int album_id: id of album to retrieve.
   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_video_from_album
---------------------

.. py:function:: read_video_from_album(album_id, video_id)

   Return *response* that contain a json that describe video

   :param int video_id: id of video to retrieve.
   :param int album_id: id of album to retrieve.
   :return: video
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


create_album
------------

.. py:function:: create_album()

   Return *response* that contain a json that describe album. This method requires a token with the "create" scope.

   :param name: The Album title
   :param description: The Album description
   :param privacy: The Album's privacy level (anybody, password)
   :param password: Required if privacy=password. The Album's password
   :param sort: The default sort order of an Album's videos (arranged, newest, oldest, plays, comments, likes, added_first, added_last, alphabetical)
   :return: album
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


update_album
------------

.. py:function:: update_album(album_id, name=None, description=None, privacy=None, password=None, sort=None)

   Return *response* that contain a json that describe album. This method requires a token with the "edit" scope.

   :param album_id:
   :param name: The Album title
   :param description: The Album description
   :param privacy: The Album's privacy level (anybody, password)
   :param password: Required if privacy=password. The Album's password
   :param sort: The default sort order of an Album's videos (arranged, newest, oldest, plays, comments, likes, added_first, added_last, alphabetical)
   :return: album
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


add_video_to_album
------------------

.. py:function:: add_video_to_album()

   Add video to album. This method requires a token with the "edit"scope.

   :param album_id:
   :param video_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


delete_album
------------

.. py:function:: delete_album(album_id)

   Delete album. This method requires a token with the "edit" scope.

   :param album_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_appearance_videos
----------------------

.. py:function:: read_appearance_videos(filter_dict=None)

   Get all videos that a user appears in.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/users#/{user_id}/appearances>`_ for details.
   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_channels
-------------

.. py:function:: read_channels(filter_dict=None)

   Get a list of all Channels.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/channels>`_ for details.
   :return: channels
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


create_channel
--------------

.. py:function:: create_channel()

   Create a new Channel.

   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_channel
------------

.. py:function:: read_channel()

   Get a channel.

   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


subscribe_channel
-----------------

.. py:function:: subscribe_channel(channel_id)

   Subscribe to a Channel.

   :param channel_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


unsubscribe_channel
-------------------

.. py:function:: unsubscribe_channel(channel_id)

   Return *response* that contain a json that describe unsubscribe_channel

   :param channel_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_groups
-----------

.. py:function:: read_groups()

   Get a list of all Groups.

   :return: groups
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_group
----------

.. py:function:: read_group(group_id)

   Get a Group.

   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


join_group
----------

.. py:function:: join_group(group_id)

   Join a Group.

   :param group_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


leave_group
-----------

.. py:function:: leave_group(group_id)

   Leave a Group.

   :param group_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_feed_videos
----------------

.. py:function:: read_feed_videos()

   Get a list of the videos in your feed.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/users#/{user_id}/feed>`_ for details.
   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_followers
--------------

.. py:function:: read_followers(filter_dict=None)

   Get a list of the user's followers.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/users#/{user_id}/followers>`_ for details.
   :return: user's followers
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_following_users
--------------------

.. py:function:: read_following_users(filter_dict=None)

   Get a list of the users that a user is following.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/users#/{user_id}/following>`_ for details.
   :return: users
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_follow_user
----------------

.. py:function:: read_followers()

   Check if a user follows another user.

   :return: user
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


follow_user
-----------

.. py:function:: follow_user(follow_user_id)

   Follow a user. This method requires a token with the "interact" scope.

   :param follow_user_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


unfollow_user
-------------

.. py:function:: unfollow_user(follow_user_id)

   Unfollow a user. This method requires a token with the "interact" scope.

   :param follow_user_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_liked_videos
-----------------

.. py:function:: read_liked_videos(video_id)

   Get a list of videos that a user likes.

   :param video_id:
   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


like_video
----------

.. py:function:: like_video(video_id)

   Like a video. This method requires a token with the "interact" scope.

   :param video_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


unlike_video
------------

.. py:function:: unlike_video(video_id)

   Unlike a video. This method requires a token with the "interact" scope.

   :param video_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_pictures
-------------

.. py:function:: read_pictures()

   Get a list of this user's portrait images.

   :return: pictures
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_portrait
-------------

.. py:function:: read_portrait(portraitset_id)

   Check if a user has a portrait.

   :param portraitset_id:
   :return: portrait
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_portfolios
---------------

.. py:function:: read_portfolios(filter_dict=None)

   Get a list of Portfolios created by a user.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/me#/portfolios>`_ for details.
   :return: portfolios
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_portfolio
--------------

.. py:function:: read_portfolio(portfolio_id)

   Get a Portfolio.

   :return portfolio_id:
   :return: portfolio
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_portfolio_videos
---------------------

.. py:function:: read_portfolio_videos(portfolio_id, filter_dict=None)

   Get the videos in this Portfolio.

   :return portfolio_id:
   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/me#/portfolios>`_ for details.
   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


read_video_from_portfolio
-------------------------

.. py:function:: read_video_from_portfolio(portfolio_id, video_id)

   Check if a Portfolio contains a video.

   :return portfolio_id:
   :return video_id:
   :return: video
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


add_video_to_portfolio
----------------------

.. py:function:: add_video_to_portfolio(portfolio_id, video_id)

   Add a video to the Portfolio. This method requires a token with the "edit" scope.

   :return portfolio_id:
   :return video_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


remove_video_from_portfolio
---------------------------

.. py:function:: remove_video_from_portfolio(portfolio_id, video_id)

   Remove a video from the Portfolio. This method requires a token with the "edit" scope.

   :return portfolio_id:
   :return video_id:
   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


get_watched_videos
------------------

.. py:function:: get_watched_videos()

   View all videos you have watched.

   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


clear_all_watch_history
-----------------------

.. py:function:: clear_all_watch_history()

   Clear your entire watch history.

   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


remove_video_from_watch_history
-------------------------------

.. py:function:: remove_video_from_watch_history()

   Remove a video from your watch history.

   :return: None
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


get_presets
-----------

.. py:function:: get_presets(filter_dict=None)

   Get all presets created by the authenticated user.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/me#/presets>`_ for details.
   :return: presets
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


get_preset
----------

.. py:function:: get_preset(preset_id)

   Get a preset.

   :param preset_id:
   :return: preset
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


update_preset
-------------

.. py:function:: update_preset(preset_id)

   Edit a preset.

   :param preset_id:
   :return: preset
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


get_preset_videos
-----------------

.. py:function:: get_preset_videos(preset_id)

   Get videos that have the provided preset.

   :param preset_id:
   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


get_videos
----------

.. py:function:: get_videos(filter_dict=None)

   Get a list of videos uploaded by a user.

   :param filter_dict: a dict with params, refer to `vimeo documentation <https://developer.vimeo.com/api/endpoints/me#/videos>`_ for details.
   :return: videos
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


get_video
---------

.. py:function:: get_video(video_id)

   Check if a user owns a clip.

   :param video_id:
   :return: video
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.


post_video
----------

.. py:function:: post_video(redirect_url, upload_url)

   Begin the video upload process. This method requires a token with the "upload" scope.


   :param redirect_url:
   :param upload_url:
   :return: video
   :rtype: requests.models.Response
   :raises BadRequestException: if HTTP code is not accepted
   :raises ClientException: raised from client. Refer to Exceptions details in this documentation.
