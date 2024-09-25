package com.example.your_project_name

import android.content.Context
import android.media.MediaRecorder
import android.view.SurfaceView
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import net.majorkernelpanic.streaming.Session
import net.majorkernelpanic.streaming.SessionBuilder
import net.majorkernelpanic.streaming.audio.AudioQuality
import net.majorkernelpanic.streaming.gl.SurfaceView
import net.majorkernelpanic.streaming.rtsp.RtspClient
import net.majorkernelpanic.streaming.video.VideoQuality
import java.io.IOException

class MainActivity: FlutterActivity() {
    private val CHANNEL = "com.example.drone_rtmp_stream"
    private lateinit var session: Session
    private lateinit var surfaceView: SurfaceView
    private var mediaRecorder: MediaRecorder? = null

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler { call, result ->
            when (call.method) {
                "connectDrone" -> {
                    // In a real application, you would implement drone connection logic here
                    result.success(true)
                }
                "startStreaming" -> {
                    val rtmpUrl = call.argument<String>("rtmpUrl")
                    if (rtmpUrl != null) {
                        startStreaming(rtmpUrl)
                        result.success(true)
                    } else {
                        result.error("INVALID_ARGUMENT", "RTMP URL is required", null)
                    }
                }
                "stopStreaming" -> {
                    stopStreaming()
                    result.success(null)
                }
                "startRecording" -> {
                    val filePath = call.argument<String>("filePath")
                    if (filePath != null) {
                        startRecording(filePath)
                        result.success(true)
                    } else {
                        result.error("INVALID_ARGUMENT", "File path is required", null)
                    }
                }
                "stopRecording" -> {
                    val filePath = stopRecording()
                    result.success(filePath)
                }
                else -> {
                    result.notImplemented()
                }
            }
        }

        // Initialize streaming session
        surfaceView = SurfaceView(this)
        session = SessionBuilder.getInstance()
            .setContext(applicationContext)
            .setAudioEncoder(SessionBuilder.AUDIO_AAC)
            .setAudioQuality(AudioQuality.HIGH)
            .setVideoEncoder(SessionBuilder.VIDEO_H264)
            .setVideoQuality(VideoQuality.DEFAULT_VIDEO_QUALITY)
            .setSurfaceView(surfaceView)
            .setPreviewOrientation(0)
            .build()
    }

    private fun startStreaming(rtmpUrl: String) {
        val rtspClient = RtspClient()
        rtspClient.setSession(session)
        rtspClient.setCallback(object : RtspClient.Callback {
            override fun onRtspUpdate(message: Int, exception: Exception?) {
                // Handle RTSP updates here
            }
        })
        rtspClient.setTransportMode(RtspClient.TRANSPORT_TCP)
        rtspClient.startStream(rtmpUrl)
    }

    private fun stopStreaming() {
        session.stop()
    }

    private fun startRecording(filePath: String) {
        mediaRecorder = MediaRecorder().apply {
            setVideoSource(MediaRecorder.VideoSource.SURFACE)
            setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
            setOutputFile(filePath)
            setVideoEncoder(MediaRecorder.VideoEncoder.H264)
            setVideoEncodingBitRate(10000000)
            setVideoFrameRate(30)
            setVideoSize(1280, 720)

            try {
                prepare()
            } catch (e: IOException) {
                e.printStackTrace()
            }

            start()
        }
    }

    private fun stopRecording(): String? {
        mediaRecorder?.apply {
            stop()
            release()
        }
        mediaRecorder = null
        return "Path/to/recorded/file.mp4" // Replace with actual file path
    }
}