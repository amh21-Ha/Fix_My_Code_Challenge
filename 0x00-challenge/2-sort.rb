def sort_args(*args)
  args.map(&:to_i).sort
end

puts sort_args(*ARGV)

