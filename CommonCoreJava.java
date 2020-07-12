public class CommonCoreJava {
	/**
		@author Gkoliver (original author), user8399 (optimization), ect (ect)
		This gets the other position of a 2-height block with 6-way orientation.
		@param posIn The blockpos in question.
		@param isTop Whether or not the block is the top half.
		@param directionIn Direction of the pos.
		@return The opposite blockpos.

		@import BlockPos net.minecraft.util.math.BlockPos
		@import Direction net.minecraft.util.Direction
	*/
	public static BlockPos getOppositePos(BlockPos posIn, boolean isTop, Direction directionIn) {
		return posIn.offset(isTop ? directionIn.getOpposite() : directionIn);
	}
}