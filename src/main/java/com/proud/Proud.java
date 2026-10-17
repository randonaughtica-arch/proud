package com.proud;

import com.proud.registry.FlagList;
import com.proud.registry.ModContent;
import net.fabricmc.api.ModInitializer;
import net.minecraft.resources.Identifier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Proud implements ModInitializer {
    public static final String MOD_ID = "proud";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    public static Identifier id(String path) {
        return Identifier.fromNamespaceAndPath(MOD_ID, path);
    }

    @Override
    public void onInitialize() {
        ModContent.register();
        LOGGER.info("Proud loaded {} flags", FlagList.FLAGS.size());
    }
}
