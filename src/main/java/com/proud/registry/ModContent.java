package com.proud.registry;

import com.proud.Proud;
import com.proud.block.FlagBlock;
import com.proud.registry.FlagList.FlagEntry;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import net.fabricmc.fabric.api.creativetab.v1.FabricCreativeModeTab;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.entity.EquipmentSlot;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.MapColor;
import net.minecraft.world.level.material.PushReaction;

/** Registers a block and item for every flag, plus one creative tab per category. */
public final class ModContent {
    private static final Map<String, List<Item>> BY_CATEGORY = new LinkedHashMap<>();

    private ModContent() {
    }

    public static void register() {
        Item blank = registerFlag("blank_flag");
        for (String category : FlagList.CATEGORIES) {
            BY_CATEGORY.put(category, new ArrayList<>());
        }
        for (FlagEntry entry : FlagList.FLAGS) {
            BY_CATEGORY.get(entry.category()).add(registerFlag(entry.id() + "_flag"));
        }

        for (Map.Entry<String, List<Item>> category : BY_CATEGORY.entrySet()) {
            List<Item> items = category.getValue();
            CreativeModeTab tab = FabricCreativeModeTab.builder()
                    .icon(() -> new ItemStack(items.isEmpty() ? blank : items.get(0)))
                    .title(Component.translatable("itemGroup." + Proud.MOD_ID + "." + category.getKey()))
                    .displayItems((parameters, output) -> {
                        output.accept(blank);
                        for (Item item : items) {
                            output.accept(item);
                        }
                    })
                    .build();
            Registry.register(BuiltInRegistries.CREATIVE_MODE_TAB, Proud.id(category.getKey()), tab);
        }
    }

    private static Item registerFlag(String path) {
        ResourceKey<Block> blockKey = ResourceKey.create(Registries.BLOCK, Proud.id(path));
        Block block = Registry.register(BuiltInRegistries.BLOCK, blockKey, new FlagBlock(BlockBehaviour.Properties.of()
                .setId(blockKey)
                .mapColor(MapColor.WOOL)
                .strength(0.5F)
                .sound(SoundType.WOOL)
                .noOcclusion()
                .ignitedByLava()
                .pushReaction(PushReaction.DESTROY)));

        ResourceKey<Item> itemKey = ResourceKey.create(Registries.ITEM, Proud.id(path));
        // Flags can be worn on the head (put one in the helmet slot); right-click still places them.
        BlockItem item = new BlockItem(block, new Item.Properties()
                .setId(itemKey)
                .useBlockDescriptionPrefix()
                .equippableUnswappable(EquipmentSlot.HEAD));
        item.registerBlocks(Item.BY_BLOCK, item);
        return Registry.register(BuiltInRegistries.ITEM, itemKey, item);
    }
}
