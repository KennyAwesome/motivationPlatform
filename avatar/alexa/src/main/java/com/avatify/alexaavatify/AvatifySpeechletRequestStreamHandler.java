package com.avatify.alexaavatify;

import com.amazon.speech.speechlet.lambda.SpeechletRequestStreamHandler;

import java.util.HashSet;
import java.util.Set;

public class AvatifySpeechletRequestStreamHandler extends SpeechletRequestStreamHandler {
    private static final Set<String> supportedApplicationIds = new HashSet<String>();
    static {
        supportedApplicationIds.add("amzn1.ask.skill.52a80932-5aaf-49bc-95ae-3e5042a18a2e");
    }

    public AvatifySpeechletRequestStreamHandler() {
        super(new AvatifySpeechlet(), supportedApplicationIds);
    }
}
